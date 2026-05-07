#!/usr/bin/env python3
"""Validate guideline topic files and README indexing."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


GUIDELINE_DIRS = {
    "cn": "yzk-guideline-cn",
    "en": "yzk-guideline-en",
}

KINDS = ("AGENTS", "CLAUDE")
LANGS = ("cn", "en")
MIXED_DOC_PATTERNS = (
    "AGENTS.md or CLAUDE.md",
    "CLAUDE.md or AGENTS.md",
    "AGENTS.md 或 CLAUDE.md",
    "CLAUDE.md 或 AGENTS.md",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate AGENTS/CLAUDE guideline topic files.",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Repository root to validate. Defaults to this script's repository.",
    )
    return parser.parse_args()


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def expected_path(root: Path, kind: str, topic: str, lang: str) -> Path:
    return root / GUIDELINE_DIRS[lang] / f"{kind}_{topic}_{lang}.md"


def discover_topics(root: Path, errors: list[str]) -> set[str]:
    topics: set[str] = set()

    for lang, dirname in GUIDELINE_DIRS.items():
        directory = root / dirname
        if not directory.is_dir():
            errors.append(f"Missing guideline directory: {rel(directory, root)}")
            continue

        for path in sorted(directory.glob("*.md")):
            match = re.fullmatch(r"(AGENTS|CLAUDE)_(.+)_(cn|en)\.md", path.name)
            if match is None:
                errors.append(f"Unexpected guideline filename: {rel(path, root)}")
                continue

            kind, topic, file_lang = match.groups()
            if file_lang != lang:
                errors.append(
                    f"Language suffix does not match directory: {rel(path, root)}"
                )
            if kind not in KINDS:
                errors.append(f"Unexpected guideline kind: {rel(path, root)}")
            topics.add(topic)

    return topics


def validate_matrix(root: Path, topics: set[str], errors: list[str]) -> None:
    for topic in sorted(topics):
        for lang in LANGS:
            for kind in KINDS:
                path = expected_path(root, kind, topic, lang)
                if not path.is_file():
                    errors.append(f"Missing expected file: {rel(path, root)}")


def validate_readme(root: Path, topics: set[str], errors: list[str]) -> None:
    readme_path = root / "README.md"
    if not readme_path.is_file():
        errors.append("Missing README.md")
        return

    readme = readme_path.read_text(encoding="utf-8")
    for topic in sorted(topics):
        if f"`{topic}`" not in readme:
            errors.append(f"README.md does not list topic `{topic}`")

        for lang in LANGS:
            for kind in KINDS:
                path = expected_path(root, kind, topic, lang)
                expected = rel(path, root)
                if expected not in readme:
                    errors.append(f"README.md does not list {expected}")


def validate_doc_type_wording(root: Path, topics: set[str], errors: list[str]) -> None:
    for topic in sorted(topics):
        for lang in LANGS:
            for kind in KINDS:
                path = expected_path(root, kind, topic, lang)
                if not path.is_file():
                    continue

                content = path.read_text(encoding="utf-8")
                for pattern in MIXED_DOC_PATTERNS:
                    if pattern in content:
                        errors.append(
                            f"{rel(path, root)} contains mixed doc wording: {pattern}"
                        )

                counterpart = "CLAUDE.md" if kind == "AGENTS" else "AGENTS.md"
                if counterpart in content:
                    errors.append(
                        f"{rel(path, root)} mentions counterpart doc name: {counterpart}"
                    )


def main() -> int:
    args = parse_args()
    root = args.root.resolve()
    errors: list[str] = []

    topics = discover_topics(root, errors)
    if not topics:
        errors.append("No guideline topics found")

    validate_matrix(root, topics, errors)
    validate_readme(root, topics, errors)
    validate_doc_type_wording(root, topics, errors)

    if errors:
        print("Guideline validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Guideline validation passed for topics: " + ", ".join(sorted(topics)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
