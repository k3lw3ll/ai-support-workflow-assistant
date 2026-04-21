# AI Support Workflow Assistant

A modular, multi-step AI workflow system that processes support tickets into structured, actionable outputs using LLM orchestration.

---

## Overview

Support and operations teams often spend significant time triaging incoming issues, identifying priorities, and drafting responses.

This project demonstrates how large language models can be orchestrated into a repeatable workflow that standardizes and accelerates that process.

Instead of a single prompt, this system uses a modular pipeline to:

- Summarize incoming requests
- Classify category and priority
- Recommend next actions
- Generate a customer-ready response

The result is a structured JSON output suitable for automation, integration, or downstream systems.

---

## Example Output

    {
      "summary": "A customer is experiencing repeated failures of their weekly analytics export...",
      "category": "Analytics Export",
      "priority": "High",
      "recommended_actions": [
        "Increase timeout settings",
        "Reduce data size",
        "Check server load"
      ],
      "response_draft": "We understand how crucial it is..."
    }

---

## Architecture

The workflow is implemented as a sequence of independent steps:

1. Summarization  
   Condenses raw ticket input into a concise problem statement

2. Classification  
   Assigns category and priority

3. Action Recommendation  
   Generates structured next steps for resolution

4. Response Drafting  
   Produces a professional customer-facing reply

Each step is modular, allowing for independent improvement and extension.

---

## Project Structure

    ai-support-workflow-assistant/
      app/
        main.py
        workflow.py
      data/
        sample_tickets/
      scripts/
        run_all.py
      output/
      requirements.txt
      README.md

---

## Getting Started

### 1. Install dependencies

    pip install -r requirements.txt

### 2. Set environment variables

Create a `.env` file in the root directory:

    OPENAI_API_KEY=your_api_key_here

### 3. Run the workflow (interactive mode)

    python app/main.py

Paste a support ticket when prompted.

### 4. Run with a sample ticket file

    python app/main.py data/sample_tickets/ticket_001.txt

### 5. Batch process all sample tickets

    python scripts/run_all.py

---

## Sample Inputs

Example tickets are included in:

    data/sample_tickets/

---

## Example Use Cases

- Support ticket triage and response drafting  
- Customer success workflows  
- Internal IT request processing  
- Operational task standardization  

---

## Key Concepts Demonstrated

- Multi-step LLM orchestration  
- Structured JSON output generation  
- Prompt design for operational workflows  
- Defensive handling of model output (JSON parsing)  
- Modular system design  
- Batch processing of inputs  

---

## Future Improvements

- Retrieval-augmented generation (Elastic / vector search)  
- Output evaluation and scoring  
- Knowledge base integration  
- Simple UI (CLI or web)  
- Model abstraction (OpenAI / Hugging Face)  

---

## Why This Matters

This project focuses on practical AI adoption:

- Turning unstructured inputs into structured outputs  
- Enabling consistent workflows across teams  
- Bridging the gap between AI capabilities and operational systems  

This pattern reflects how AI is increasingly implemented in enterprise environments: as structured workflows rather than standalone prompts.

---

## Author

Ken Elwell