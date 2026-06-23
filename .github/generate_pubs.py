#!/usr/bin/env python3
"""Generate a ## Publications section for README from BibTeX headers in pubs/*_full.md files.

Usage:
  python .github/generate_pubs.py                                    # Update README.md in place (default)
  python .github/generate_pubs.py --stdout                           # Print to stdout, don't modify file
  python .github/generate_pubs.py --group-by-year                    # Group under year subheadings (### 2026, etc.)
  python .github/generate_pubs.py --et-al 2                          # List up to 2 authors before "et al."
  python .github/generate_pubs.py --readme path/to/file.md           # Target a different README file
  python .github/generate_pubs.py --pubs-dir path/to/pubs           # Path to pubs directory (default: pubs)
  python .github/generate_pubs.py -h                                 # Show full help

The script extracts BibTeX blocks from the top of each pubs/*_full.md file,
formats citations with ISO 4 journal abbreviations, and inserts/replaces the
publications section between <!-- PUBLICATIONS_START --> and <!-- PUBLICATIONS_END -->
markers in the target README.

Link paths are computed as relative paths from the README's directory to the
pubs directory, so the script works correctly regardless of where the README
and pubs directories are located.
"""

import glob
import os
import re
import sys

import bibtexparser
from bibtexparser.bparser import BibTexParser

SECTION_START = "<!-- PUBLICATIONS_START -->"
SECTION_END = "<!-- PUBLICATIONS_END -->"

# Extract BibTeX block from the top of a _full.md file
BIBTEX_RE = re.compile(r"```\s*\n(@.*?)\n```", re.DOTALL)


def extract_bibtex(path: str) -> str | None:
    with open(path) as f:
        text = f.read()
    m = BIBTEX_RE.match(text)
    if m:
        return m.group(1)
    return None


def normalize_author(author: str) -> str:
    """Convert 'First Middle Last' to 'Last, F.M.' format."""
    author = re.sub(r"{\\'(\w)}", r"\1", author)
    author = re.sub(r"\\'(\w)", r"\1", author)
    author = re.sub(r"[{}\\]", "", author)

    parts = author.strip().split()
    if len(parts) == 1:
        return parts[0]

    surname = parts[-1]
    initials = [g.strip(".")[0].upper() + "." for g in parts[:-1] if g.strip(".")]

    if initials:
        return f"{surname}, {''.join(initials)}"
    return surname


def format_authors(author_str: str, max_before_et_al: int = 3) -> str:
    authors = [normalize_author(a.strip()) for a in author_str.split(" and ")]
    if len(authors) > max_before_et_al:
        return f"{authors[0]} et al."
    return ", ".join(authors)


def clean_field(value: str) -> str:
    value = value.strip("{}")
    value = value.replace("\n", " ")
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def abbreviate_journal(title: str) -> str:
    """Abbreviate journal title using ISO 4 rules via pyiso4."""
    from pyiso4.ltwa import Abbreviate
    abbr = Abbreviate.create()
    # Title-case but preserve all-uppercase acronyms (e.g., IEEE)
    titled = re.sub(
        r"[A-Za-z]+",
        lambda m: m.group() if m.group().isupper() else m.group().title(),
        title,
    )
    return abbr(titled)


def build_links(base: str, pubs_dir: str, readme_dir: str) -> str:
    parts = []
    for suffix, label in [
        ("_full.md", "full text"),
        ("_main.md", "main"),
        ("_backmatter.md", "backmatter"),
        ("_appendix.md", "appendix"),
    ]:
        abs_path = os.path.join(pubs_dir, f"{base}{suffix}")
        if os.path.exists(abs_path):
            # Compute relative path from README dir to pubs file
            rel_path = os.path.relpath(abs_path, readme_dir)
            parts.append(f"[{label}]({rel_path})")
    return " | ".join(parts)


def generate_publications(pubs_dir: str, readme_dir: str, group_by_year: bool = False, max_before_et_al: int = 3) -> str:
    full_files = sorted(glob.glob(os.path.join(pubs_dir, "*_full.md")))
    if not full_files:
        return "_No publications yet._\n"

    entries = []
    for full_path in full_files:
        bib_text = extract_bibtex(full_path)
        if bib_text is None:
            print(f"Warning: no BibTeX block in {full_path}, skipping.", file=sys.stderr)
            continue

        parser = BibTexParser(common_strings=True)
        bib_db = bibtexparser.loads(bib_text, parser=parser)

        for entry in bib_db.entries:
            authors = format_authors(entry.get("author", ""), max_before_et_al=max_before_et_al)
            title = clean_field(entry.get("title", ""))
            journal = abbreviate_journal(clean_field(entry.get("journal", "")))
            year = entry.get("year", "")
            volume = entry.get("volume", "")
            pages = clean_field(entry.get("pages", ""))
            doi = entry.get("doi", "")
            url = entry.get("url", "")

            link = f"https://doi.org/{doi}" if doi else url
            base = os.path.basename(full_path).replace("_full.md", "")

            citation = f"- {authors} (**{year}**). **{title}**"
            if journal:
                citation += f" *{journal}*"
            if volume:
                citation += f", {volume}"
            if pages:
                citation += f", {pages}"
            citation += "."

            links = build_links(base, pubs_dir, readme_dir)
            if links:
                citation += f"<br>\n  {links}"

            entries.append((year, citation))

    if not entries:
        return "_No publications yet._\n"

    if group_by_year:
        from collections import OrderedDict
        by_year = OrderedDict()
        for year, citation in entries:
            by_year.setdefault(year, []).append(citation)

        lines = []
        for year, citations in by_year.items():
            lines.append(f"### {year}")
            lines.append("")
            lines.extend(citations)
            lines.append("")
        return "\n".join(lines)

    return "\n".join(c for _, c in entries) + "\n"


def update_readme(content: str, readme_path: str, in_place: bool) -> str | None:
    """Update the publications section in the README.

    If in_place is True, write to the file and return None.
    If in_place is False, return the new content as a string.
    """
    if in_place:
        with open(readme_path) as f:
            readme_content = f.read()
    else:
        readme_content = ""

    new_section = f"{SECTION_START}\n## Publications\n\n{content}{SECTION_END}"

    if in_place:
        # Case 1: markers exist — replace between them
        marker_pattern = re.compile(
            re.escape(SECTION_START) + r".*?" + re.escape(SECTION_END),
            re.DOTALL,
        )
        if marker_pattern.search(readme_content):
            result = marker_pattern.sub(new_section, readme_content)
        else:
            # Case 2: existing ## Publications heading (no markers)
            pubs_pattern = re.compile(
                r"^## Publications\s*\n(.*?)(?=\n## |\Z)",
                re.DOTALL | re.MULTILINE,
            )
            if pubs_pattern.search(readme_content):
                result = pubs_pattern.sub(new_section.rstrip("\n") + "\n", readme_content)
            else:
                # Case 3: no publications section at all — append
                result = readme_content.rstrip() + "\n\n" + new_section + "\n"

        with open(readme_path, "w") as f:
            f.write(result)
        print(f"Updated {readme_path} with publications.")
        return None

    # Not in place — return just the publications section
    return f"## Publications\n\n{content}"


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Generate publications section for README")
    parser.add_argument("--pubs-dir", type=str, default="pubs",
                        help="Path to directory containing pubs (default: pubs)")
    parser.add_argument("--readme", type=str, default="README.md",
                        help="Path to README.md (default: README.md)")
    parser.add_argument("--group-by-year", action="store_true",
                        help="Group publications under year subheadings")
    parser.add_argument("--et-al", type=int, default=3, dest="et_al",
                        help="Max authors listed before 'et al.' (default: 3)")
    parser.add_argument("--in-place", action="store_true", default=True,
                        help="Modify the README file in place (default)")
    parser.add_argument("--stdout", action="store_true",
                        help="Print result to stdout instead of writing to file")
    args = parser.parse_args()

    pubs_dir = os.path.abspath(args.pubs_dir)
    readme_dir = os.path.dirname(os.path.abspath(args.readme))

    pubs_content = generate_publications(
        pubs_dir=pubs_dir,
        readme_dir=readme_dir,
        group_by_year=args.group_by_year,
        max_before_et_al=args.et_al,
    )
    in_place = args.in_place and not args.stdout
    result = update_readme(pubs_content, args.readme, in_place)

    if result is not None:
        print(result)


if __name__ == "__main__":
    main()
