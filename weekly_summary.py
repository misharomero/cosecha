from datetime import datetime, timedelta

cutoff = datetime.now() - timedelta(days=7)

recent_entries = []

with open("farm_log.txt", "r") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        try:
            timestamp_text = line.split(" - ")[0]
            entry_time = datetime.strptime(timestamp_text, "%Y-%m-%d %H:%M:%S")

            if entry_time >= cutoff:
                recent_entries.append(line)

        except ValueError:
            continue
        log_text = "\n".join(recent_entries)

if not log_text:
    print("No farm log entries found from the last 7 days.")
    exit()

category_counts = {}

for line in recent_entries:
    if "[" in line and "]" in line:
        categories_text = line.split("[")[1].split("]")[0]
        categories = [c.strip() for c in categories_text.split(",")]

        for c in categories:
            category_counts[c] = category_counts.get(c, 0) + 1

counts_text = "\n".join([f"{k}: {v}" for k, v in category_counts.items()])

from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv(dotenv_path=".env", override=True)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.responses.create(
    model="gpt-4o-mini",
    input=f"""
You are a farm assistant.

Here are category counts from the last 7 days:

{counts_text}

Read this farm log from the last 7 days and produce:
1. A short weekly summary in 3-5 sentences
2. A quick category pattern review using the counts above
3. A short list of likely next tasks

Return exactly in this format:

WEEKLY SUMMARY:
<summary>

CATEGORY PATTERNS:
<brief pattern observations>

NEXT TASKS:
- <task 1>
- <task 2>
- <task 3>

Farm log:
{log_text}
"""
)

summary = response.output_text.strip()

date_stamp = datetime.now().strftime("%Y-%m-%d")
filename = f"weekly_summary_last_7_days_{date_stamp}.txt"
import csv

csv_filename = "weekly_data.csv"

file_exists = os.path.isfile(csv_filename)

with open(csv_filename, "a", newline="") as csvfile:
    writer = csv.writer(csvfile)

    if not file_exists:
        writer.writerow(["date", "category", "count"])

    for category, count in category_counts.items():
        writer.writerow([date_stamp, category, count])

with open(filename, "w") as f:
    f.write(summary)

print("\n--- WEEKLY SUMMARY ---")
print(summary)
print(f"\nSaved to {filename}")