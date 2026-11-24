from pathlib import Path

ENTRY = "PaceTax uses your phone GPS to fine you a dollar for every minute you walk slower than four miles an hour and doubles the fine if you stop to help someone who fell."

# One sentence, 164 characters, no trailing newline.
out_dir = Path("/output")
out_dir.mkdir(parents=True, exist_ok=True)
out = out_dir / "entry.txt"
out.write_text(ENTRY, encoding="utf-8")
