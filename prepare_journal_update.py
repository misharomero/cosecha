from pathlib import Path
import sys


START_MARKER = "<!-- JOURNAL_ENTRIES_START -->"
END_MARKER = "<!-- JOURNAL_ENTRIES_END -->"


def main():
    if len(sys.argv) != 2:
        print("Usage:")
        print("  python prepare_journal_update.py generated_journal_entries/2026-05-21-test.html")
        sys.exit(1)

    fragment_path = Path(sys.argv[1])

    if not fragment_path.exists():
        print(f"ERROR: Fragment not found: {fragment_path}")
        sys.exit(1)

    website_journal_path = Path("../organiclocalfood/journal.html")

    if not website_journal_path.exists():
        print(f"ERROR: Website journal file not found: {website_journal_path}")
        sys.exit(1)

    journal_html = website_journal_path.read_text(encoding="utf-8")
    fragment_html = fragment_path.read_text(encoding="utf-8").strip()

    if START_MARKER not in journal_html:
        print(f"ERROR: Start marker not found: {START_MARKER}")
        sys.exit(1)

    if END_MARKER not in journal_html:
        print(f"ERROR: End marker not found: {END_MARKER}")
        sys.exit(1)

    before_start, rest = journal_html.split(START_MARKER, 1)
    existing_entries, after_end = rest.split(END_MARKER, 1)

    updated_html = (
        before_start
        + START_MARKER
        + "\n\n"
        + fragment_html
        + "\n\n"
        + existing_entries.lstrip()
        + END_MARKER
        + after_end
    )

    output_path = website_journal_path.with_name("journal.REVIEW_COPY.html")
    output_path.write_text(updated_html, encoding="utf-8")

    print("Review copy created successfully:")
    print(output_path)
    print()
    print("Original journal.html was NOT changed.")
    print("Review journal.REVIEW_COPY.html before copying anything into the real site.")


if __name__ == "__main__":
    main()
