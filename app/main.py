import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from workflow import (
    summarize_ticket,
    classify_ticket,
    recommend_actions,
    draft_response,
)

print("Script is running...")
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
print("API key loaded:", bool(api_key))

client = OpenAI(api_key=api_key)


def process_ticket(ticket_text: str) -> dict:
    summary = summarize_ticket(client, ticket_text)
    classification = classify_ticket(client, summary)
    actions = recommend_actions(client, summary)
    response = draft_response(client, summary, classification["priority"])

    result = {
        "summary": summary,
        "category": classification["category"],
        "priority": classification["priority"],
        "recommended_actions": actions,
        "response_draft": response,
    }

    return result


if __name__ == "__main__":
    ticket = input("Paste support ticket text:\n\n")
    result = process_ticket(ticket)

    print("\n=== JSON RESULT ===\n")
    print(json.dumps(result, indent=2))

    os.makedirs("output", exist_ok=True)
    with open("output/latest_result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print("\nSaved result to output/latest_result.json")