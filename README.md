# AI Support Workflow Assistant

A lightweight, multi-step AI workflow system that processes support requests and produces structured, actionable outputs for operations teams.

## Overview

Support and operations teams often spend significant time triaging incoming issues, identifying priorities, and drafting responses. This project demonstrates how large language models can be orchestrated into a repeatable workflow that standardizes and accelerates that process.

Instead of a single prompt, this system uses a modular pipeline to:
- summarize incoming requests
- classify category and priority
- recommend next actions
- generate a customer-ready response

The result is a structured JSON output that can be used for automation, integration, or downstream systems.

## Example Output

```json
{
  "summary": "...",
  "category": "Access Issue",
  "priority": "High",
  "recommended_actions": [
    "Check SSO configuration",
    "Verify user account status"
  ],
  "response_draft": "..."
}

Architecture

The workflow is implemented as a sequence of independent steps:

Summarization
Condenses raw ticket input into a concise problem statement
Classification
Assigns category and priority
Action Recommendation
Generates a structured set of next steps for resolution
Response Drafting
Produces a professional customer-facing reply

Each step is implemented as a separate function, enabling modular improvement and extension.

Project Structure
ai-support-workflow-assistant/
  app/
    main.py
    workflow.py
  data/
    sample_tickets/
  output/
  requirements.txt
  README.md

  Getting Started

1. Install dependencies

pip install -r requirements.txt

2. Set environment variables

Create a .env file:

OPENAI_API_KEY=your_api_key_here

3. Run the workflow

python app/main.py

Paste a support ticket when prompted.

Sample Inputs

Example tickets are included in:

data/sample_tickets/

Key Concepts Demonstrated
Multi-step LLM orchestration
Structured JSON output generation
Prompt design for operational workflows
Defensive handling of model output (JSON parsing)
Modular workflow design for extensibility
Future Improvements
Retrieval-augmented generation (Elastic / vector search)
Evaluation and scoring of outputs
Batch processing of tickets
Simple UI for interaction (CLI or web)
Model abstraction (OpenAI / Hugging Face backends)
Why This Matters

This project focuses on practical AI adoption:

turning unstructured inputs into structured outputs
enabling consistent workflows across teams
bridging the gap between AI capabilities and operational use

It reflects real-world patterns used in enterprise AI systems, particularly in support, customer success, and internal operations.

Author

Ken Elwell