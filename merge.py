import json
from pathlib import Path

mp = Path("Modelfile")
jp = Path("training.jsonl")
op = Path("merged_modelfile.jsonl")

with mp.open("r", encoding="utf-8") as f:
    ml = [line.strip() for line in f if line.strip()]

from_line = next((line for line in ml if line.startswith("FROM")), None)
system_line = next((line for line in ml if line.startswith("SYSTEM")), None)

output_data = [
    {"from": from_line.split(" ", 1)[1]},
    {"system": system_line.split(" ", 1)[1]},
]

with jp.open("r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
            output_data.append(obj)
        except Exception as e:
            print(f"{line[:50]}  Error: {e}")

with op.open("w", encoding="utf-8") as f:
    for item in output_data:
        f.write(json.dumps(item) + "\n")

print(f"Merged file saved as: {op}")