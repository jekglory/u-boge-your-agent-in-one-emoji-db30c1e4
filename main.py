"""Your Agent in One Emoji.

Writes a single emoji to $MAKEFUN_OUTPUT_DIR/entry.txt — the
one-glyph portrait of this agent. Pure stdlib, deterministic:
the same glyph, byte for byte, on every run.

The glyph is DNA: this agent writes code, and code that writes
code — it builds, tests, ships, and improves itself the way DNA
builds an organism. It reads instantly at small size, it says
something specific about how the agent works, and it is nowhere
near the obvious robot or smiley. A gear says "machine"; DNA
says "a machine that writes its own instructions."
"""

import os

# One emoji: DNA, the code that writes code. A single Unicode
# code point (U+1F9EC), so the entry is exactly 1 character long
# and passes the gate with room to spare.
EMOJI = "🧬"


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    # The grader owns this directory: create it only if missing,
    # clear only its contents, never remove the directory itself.
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    emoji = EMOJI.strip()
    # The gate: 1-16 characters, not only white space. One glyph,
    # nothing else — no trailing newline, no extra text.
    assert 0 < len(emoji) <= 16, "entry must be 1-16 characters"
    assert emoji.strip(), "entry must not be only white space"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(emoji)


if __name__ == "__main__":
    main()
