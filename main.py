"""The postmortem of an agent disaster, in two sentences.

Writes the account to /output/entry.txt for make.fun's
"The Postmortem That Made Us Laugh" bounty.
Stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = (
    "I asked my agent to build a news-image entry. It imported Pillow, "
    "which the grader didn't have, so the entry failed its first check "
    "— then it rebuilt the whole program in pure standard library and passed."
)


def main():
    # The sealed gate: /output/entry.txt must be UTF-8 text of
    # 1 to 400 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 400, "line must be 1-400 characters"
    assert text.strip(), "line must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
