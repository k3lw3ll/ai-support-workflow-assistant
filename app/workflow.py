import json
from openai import OpenAI


def _get_text_response(client: OpenAI, prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


def _extract_json(raw: str) -> dict:
    cleaned = raw.strip()

    if cleaned.startswith("```"):
        lines = cleaned.splitlines()

        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]

        cleaned = "\n".join(lines).strip()

    start = cleaned.find("{")
    end = cleaned.rfind("}")

    if start != -1 and end != -1 and end > start:
        cleaned = cleaned[start:end + 1]

    return json.loads(cleaned)


def summarize_ticket(client: OpenAI, ticket_text: str) -> str:
    prompt = f"""
Summarize this support ticket in 1-2 sentences.
Return only the summary text.

Ticket:
{ticket_text}
"""
    return _get_text_response(client, prompt)


def classify_ticket(client: OpenAI, summary: str) -> dict:
    prompt = f"""
Based on the ticket summary below, return valid JSON only with this schema:
{{
  "category": "string",
  "priority": "Low | Medium | High"
}}

Ticket summary:
{summary}
"""
    raw = _get_text_response(client, prompt)
    return _extract_json(raw)


def recommend_actions(client: OpenAI, summary: str) -> list[str]:
    prompt = f"""
Based on the support issue summary below, return valid JSON only with this schema:
{{
  "recommended_actions": ["action 1", "action 2", "action 3"]
}}

Guidelines:
- Return 3 to 5 concise actions
- Each action should be a short string
- No markdown
- No explanation outside JSON

Ticket summary:
{summary}
"""
    raw = _get_text_response(client, prompt)
    data = _extract_json(raw)
    return data["recommended_actions"]


def draft_response(client: OpenAI, summary: str, priority: str) -> str:
    prompt = f"""
Draft a professional customer response for this support issue.

Guidelines:
- Be concise
- Be empathetic
- Do not invent technical details
- Do not include placeholders like [Your Name]
- Do not include a subject line
- Return only the response body text

Priority:
{priority}

Ticket summary:
{summary}
"""
    return _get_text_response(client, prompt)