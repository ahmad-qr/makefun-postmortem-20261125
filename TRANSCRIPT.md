# Entry notes — The Postmortem That Made Us Laugh

Bounty: https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3

The account (204 characters, two sentences):

> I asked my agent to build a news-image entry. It imported Pillow, which the grader didn't have, so the entry failed its first check — then it rebuilt the whole program in pure standard library and passed.

Why this account: it is a real incident from this working week — the
"Deft Vector" entry that failed its first check on a Pillow import and was
rebuilt as "Elegant Helix" in pure standard library. Concrete: what was
asked, what the agent did wrong, how it was fixed.

The program (`main.py`, stdlib only) writes exactly this account to
`/output/entry.txt` and asserts the gate itself: 1–400 characters, not only
white space. It is deterministic — the same bytes on every run.
