from pathlib import Path

ENTRY = "WillDraft rewrites your will every time you skip the gym, emails the newest version to your least favourite relative, and charges your estate per draft until your children inherit a gym membership and a stranger."

# One sentence, 212 characters, no trailing newline.
def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
