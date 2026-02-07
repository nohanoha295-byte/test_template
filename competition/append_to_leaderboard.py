import csv
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "leaderboard" / "leaderboard.csv"

def main(team, model, score, notes=""):
    exists = CSV_PATH.exists()

    with CSV_PATH.open("a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not exists:
            writer.writerow([
                "team", "model", "score", "timestamp_utc", "notes"
            ])

        writer.writerow([
            team,
            model,
            f"{float(score):.8f}",
            datetime.utcnow().isoformat() + "Z",
            notes
        ])

if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])