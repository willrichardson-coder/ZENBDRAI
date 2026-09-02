#!/usr/bin/env python3
"""Validate the shareable framework using only the Python standard library."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md",
    "README.md",
    "START_HERE.md",
    "SETUP_INSTRUCTIONS.md",
    "CONTRIBUTING.md",
    "00_My_Workspace/README.md",
    "00_My_Workspace/MY_ASSIGNMENTS.template.md",
    "01_Rules/zendesk-account-to-outreach-rules.md",
    "01_Rules/email-outreach-drafting-standard.md",
    "02_Knowledge/enterprise-bdr-operating-controls.md",
    ".github/CODEOWNERS",
)
TEXT_SUFFIXES = {".md", ".txt", ".yml", ".yaml", ".json", ".csv"}


def repository_files() -> list[str]:
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [line for line in result.stdout.splitlines() if line]


def main() -> int:
    errors: list[str] = []

    for relative_path in REQUIRED:
        if not (ROOT / relative_path).is_file():
            errors.append(f"Missing required file: {relative_path}")

    tracked = repository_files()
    forbidden_tracked = {
        "00_My_Workspace/MY_ASSIGNMENTS.md",
    }
    for relative_path in tracked:
        if relative_path in forbidden_tracked or relative_path.startswith("08_Working_Accounts/"):
            errors.append(f"Local account work is tracked: {relative_path}")

    files_to_check = set(tracked).union(REQUIRED)
    for relative_path in sorted(files_to_check):
        path = ROOT / relative_path
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "\N{EM DASH}" in text:
            errors.append(f"Em dash found: {relative_path}")

    template = ROOT / "00_My_Workspace/MY_ASSIGNMENTS.template.md"
    if template.is_file():
        required_headers = (
            "Account name",
            "CRM Account ID",
            "Website",
            "Aligned AE",
            "Motion",
            "Priority",
        )
        template_text = template.read_text(encoding="utf-8")
        for header in required_headers:
            if header not in template_text:
                errors.append(f"Assignment template is missing column: {header}")

    if errors:
        print("Framework validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Framework validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
