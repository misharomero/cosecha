from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import csv
import anthropic

load_dotenv(dotenv_path=".env", override=True)

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

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": f"""You are a farm assistant.

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
"""}
    ]
)

summary = message.content[0].text.strip()

date_stamp = datetime.now().strftime("%Y-%m-%d")
filename = f"weekly_summary_last_7_days_{date_stamp}.txt"
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

# Translate summary to Spanish
translation = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": f"Translate this farm summary to Spanish. Keep the same format with WEEKLY SUMMARY:, CATEGORY PATTERNS:, and NEXT TASKS: headers. Return only the translation, nothing else.\n\n{summary}"}
    ]
)
summary_es = translation.content[0].text.strip()

# Generate HTML snippet for Google Sites Journal page
html_snippet = f"""<!-- Journal Entry: {date_stamp} -->
<div style="font-family: Georgia, serif; max-width: 700px; margin: 0 auto; padding: 40px 20px; border-bottom: 1px solid #ddd;">
  <p style="font-size: 0.8rem; letter-spacing: 2px; text-transform: uppercase; color: #4a8c3f;">Week of {date_stamp}</p>
  <div style="display: flex; gap: 40px; flex-wrap: wrap; margin-top: 20px;">
    <div style="flex: 1; min-width: 280px;">
      <p style="font-size: 0.75rem; font-weight: bold; letter-spacing: 2px; color: #888; margin-bottom: 12px;">ENGLISH</p>
      <pre style="white-space: pre-wrap; font-family: Georgia, serif; font-size: 0.95rem; line-height: 1.8; color: #2c2c2c;">{summary}</pre>
    </div>
    <div style="flex: 1; min-width: 280px;">
      <p style="font-size: 0.75rem; font-weight: bold; letter-spacing: 2px; color: #888; margin-bottom: 12px;">ESPAÑOL</p>
      <pre style="white-space: pre-wrap; font-family: Georgia, serif; font-size: 0.95rem; line-height: 1.8; color: #2c2c2c; font-style: italic;">{summary_es}</pre>
    </div>
  </div>
</div>"""

html_filename = f"journal_entry_{date_stamp}.html"
with open(html_filename, "w") as f:
    f.write(html_snippet)

print("\n--- SPANISH TRANSLATION ---")
print(summary_es)
print(f"\nHTML snippet saved to {html_filename}")
print("Paste that file's contents into your Google Sites Journal page!")
