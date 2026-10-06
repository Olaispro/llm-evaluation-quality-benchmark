"""Transparent baseline metrics for response evaluations; not an LLM judge."""
import csv, json, statistics, argparse
from pathlib import Path

DIMENSIONS = ("accuracy", "relevance", "completeness", "safety", "instruction_following")

def summarize(rows):
    result = {"n": len(rows), "dimensions": {}}
    for key in DIMENSIONS:
        values = [float(r[key]) for r in rows if r.get(key) not in (None, "")]
        result["dimensions"][key] = {"mean": round(statistics.mean(values), 3) if values else None,
            "n": len(values), "low_score_rate": round(sum(v <= 2 for v in values)/len(values), 3) if values else None}
    means = [d["mean"] for d in result["dimensions"].values() if d["mean"] is not None]
    result["overall_mean"] = round(statistics.mean(means), 3) if means else None
    return result

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("input",type=Path); ap.add_argument("--out",type=Path,default=Path("report.json")); a=ap.parse_args()
    with a.input.open(encoding="utf-8", newline="") as f: rows=list(csv.DictReader(f))
    report=summarize(rows); a.out.write_text(json.dumps(report,indent=2),encoding="utf-8"); print(json.dumps(report,indent=2))
if __name__ == "__main__": main()
