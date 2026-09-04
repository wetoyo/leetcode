#!/usr/bin/env python3
"""
Prompt for a LeetCode problem URL and populate the headers in
today/README.md, today/Solution.cs, and today/solution.py.

If a file is missing from today/ (e.g. right after the nightly rotation),
it is first copied over from templates/ before its header is filled in.
Run from anywhere; paths are resolved relative to this script's location.

Usage:
    python templates/new_problem.py
"""

import json
import re
import shutil
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = REPO_ROOT / "templates"
TODAY_DIR = REPO_ROOT / "today"

SLUG_RE = re.compile(r"/problems/([a-z0-9-]+)/?")

GRAPHQL_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    difficulty
    topicTags { name }
  }
}
"""


def extract_slug(url: str) -> str:
    match = SLUG_RE.search(url)
    if not match:
        print(f"Could not find a /problems/<slug>/ segment in: {url}")
        sys.exit(1)
    return match.group(1)


def fetch_metadata(slug: str) -> dict:
    body = json.dumps(
        {"query": GRAPHQL_QUERY, "variables": {"titleSlug": slug}}
    ).encode("utf-8")
    request = urllib.request.Request(
        "https://leetcode.com/graphql/",
        data=body,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
            "Referer": f"https://leetcode.com/problems/{slug}/",
        },
    )
    with urllib.request.urlopen(request, timeout=10) as response:
        payload = json.loads(response.read())
    question = payload.get("data", {}).get("question")
    if not question:
        raise ValueError(f"LeetCode API returned no data for slug '{slug}'")
    return {
        "number": question["questionFrontendId"],
        "title": question["title"],
        "difficulty": question["difficulty"],
        "topics": ", ".join(tag["name"] for tag in question["topicTags"]),
    }


def prompt_manual_metadata(slug: str) -> dict:
    print("Falling back to manual entry.")
    return {
        "number": input("Problem number: ").strip(),
        "title": input("Title: ").strip(),
        "difficulty": input("Difficulty: ").strip(),
        "topics": input("Topics (comma-separated, optional): ").strip(),
    }


def ensure_today_file(name: str) -> Path:
    target = TODAY_DIR / name
    if not target.exists():
        TODAY_DIR.mkdir(exist_ok=True)
        shutil.copyfile(TEMPLATES_DIR / name, target)
        print(f"Copied templates/{name} -> today/{name}")
    return target


def update_readme(meta: dict, slug: str) -> None:
    path = ensure_today_file("README.md")
    content = path.read_text(encoding="utf-8")

    content = re.sub(
        r"^#.*$", f"# {meta['title']}", content, count=1, flags=re.MULTILINE
    )
    content = re.sub(
        r"^\[LeetCode #.*\]\(https://leetcode\.com/problems/[^)]*\).*$",
        f"[LeetCode #{meta['number']}](https://leetcode.com/problems/{slug}/) "
        f"— Difficulty: {meta['difficulty']}",
        content,
        count=1,
        flags=re.MULTILINE,
    )

    path.write_text(content, encoding="utf-8")
    print(f"Updated {path.relative_to(REPO_ROOT)}")


def update_cs(meta: dict, slug: str) -> None:
    path = ensure_today_file("Solution.cs")
    content = path.read_text(encoding="utf-8")

    header = (
        f"// LeetCode #{meta['number']} - {meta['title']}\n"
        f"// https://leetcode.com/problems/{slug}/\n"
        f"//\n"
        f"// Difficulty: {meta['difficulty']}\n"
        f"// Topics: {meta['topics']}\n"
        f"//\n"
        f"// Approach:\n"
        f"//\n"
        f"// Time:  O()\n"
        f"// Space: O()\n"
    )

    existing_header = re.match(r"(?:^//.*\n)+", content, flags=re.MULTILINE)
    if existing_header:
        content = header + content[existing_header.end() :]
    else:
        content = header + "\n" + content

    path.write_text(content, encoding="utf-8")
    print(f"Updated {path.relative_to(REPO_ROOT)}")


def update_py(meta: dict, slug: str) -> None:
    path = ensure_today_file("solution.py")
    content = path.read_text(encoding="utf-8")

    header = (
        f'"""\n'
        f"LeetCode #{meta['number']} - {meta['title']}\n"
        f"https://leetcode.com/problems/{slug}/\n"
        f"\n"
        f"Difficulty: {meta['difficulty']}\n"
        f"Topics: {meta['topics']}\n"
        f"\n"
        f"Approach:\n"
        f"\n"
        f"\n"
        f"Time:  O()\n"
        f"Space: O()\n"
        f'"""\n'
    )

    existing_header = re.match(r'\A""".*?"""\n', content, flags=re.DOTALL)
    if existing_header:
        content = header + content[existing_header.end() :]
    else:
        content = header + "\n\n" + content

    path.write_text(content, encoding="utf-8")
    print(f"Updated {path.relative_to(REPO_ROOT)}")


def main() -> None:
    url = input("LeetCode problem URL: ").strip()
    slug = extract_slug(url)

    try:
        meta = fetch_metadata(slug)
    except (urllib.error.URLError, ValueError, TimeoutError, OSError) as exc:
        print(f"Could not fetch problem metadata automatically: {exc}")
        meta = prompt_manual_metadata(slug)

    update_readme(meta, slug)
    update_cs(meta, slug)
    update_py(meta, slug)


if __name__ == "__main__":
    main()
