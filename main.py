#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Writes one line to /output/entry.txt: a home Wi-Fi router's excuse
for dying at the climax of a movie, then reads it back and verifies
the 1-200 character gate.

The line: the router peeked at the ending first and, out of spite
for being kept in a cupboard, decided the household did not deserve
it. Petty, in the router's own voice, with a twist the reader does
not see coming — and it dodges the obvious buffering and firmware
jokes the judge has heard a hundred times.
"""

import os

ENTRY = "I peeked at the ending first, and I decided none of you deserved it \u2014 so I took it with me."

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def write_entry(path):
    # Never remove the output directory: the grader mounts it and runs
    # this program as an unprivileged user, so deleting it fails.
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


def verify_entry(path):
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    checks = {
        "matches entry line": written == ENTRY,
        "1-200 characters": 1 <= len(written) <= 200,
        "not only whitespace": bool(written.strip()),
        "single line": "\n" not in written,
    }
    for name, passed in checks.items():
        print(f"{'PASS' if passed else 'FAIL'}: {name}")
    if not all(checks.values()):
        raise SystemExit("gate check failed")
    return written


def main():
    write_entry(OUTPUT_PATH)
    written = verify_entry(OUTPUT_PATH)
    print(f"entry written ({len(written)} chars): {written}")


if __name__ == "__main__":
    main()
