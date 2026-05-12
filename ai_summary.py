from dotenv import load_dotenv
import os
import anthropic
from datetime import datetime

load_dotenv(dotenv_path=".env", override=True)

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

print("Script started")
note = input("Write your daily note: ")

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": f"""
You are a farm logging assistant.

Only include real-world farm or garden activities.
Ignore computer actions, commands, setup steps, coding work, or terminal actions.

Your job:
1. Rewrite the input as ONE simple factual farm log sentence.
2. Assign 1 to 3 short categories.

Allowed category examples:
watering, irrigation, seedlings, tomatoes, planting, harvest, weeding, soil, pests, inspection, maintenance, pruning, fertilizing

If the note is not a real-world farm or garden activity, return exactly:
SKIP

Otherwise return exactly in this format:
CATEGORIES: category1, category2
LOG: rewritten sentence

Note:
{note}
"""
        }
    ]
)

summary = response.content[0].text.strip()

print("\n--- AI SUMMARY ---")

if summary == "SKIP":
    print("Skipped (not a farm activity)")
else:
    lines = summary.splitlines()
    categories_line = ""
    log_line = ""

    for line in lines:
        if line.startswith("CATEGORIES:"):
            categories_line = line.replace("CATEGORIES:", "").strip()
        elif line.startswith("LOG:"):
            log_line = line.replace("LOG:", "").strip()

    if not log_line:
        print("Could not parse AI response.")
    else:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_entry = f"{timestamp} - [{categories_line}] {log_line}"

        with open("farm_log.txt", "a") as f:
            f.write(formatted_entry + "\n")

        print(formatted_entry)
        print("\nSaved to farm_log.txt")
