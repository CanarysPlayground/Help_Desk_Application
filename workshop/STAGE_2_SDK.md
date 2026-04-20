# Stage 2: SDK — Code-aware agent steps

> **Related Exercises:** 
> - [Exercise 2: Plan Assign Feature](exercises/EXERCISE_2_PLAN_ASSIGN_FEATURE.md)
> - [Exercise 4: Self-Healing with SDK](exercises/EXERCISE_4_SELF_HEALING.md)

Goal: Install and use the Copilot SDK to add repo-aware analysis and intelligence to the CRM.

## Install Copilot SDK
- Repo: https://github.com/github/copilot-sdk
- Follow the README to install and set up the SDK in your environment.
- Ensure permissions for repo read/write, PR creation, and limited command execution (lint/tests).

## Steps
- Scaffold: Create an extension that reads the workspace, runs searches, and proposes diffs.
- Analyze: Implement a command that scans for API/Schema mismatches (e.g., `TicketResponse.ticket_id` vs model `id`) and suggests a minimal patch.
- Patch & PR: Apply changes to `app/schemas/ticket.py`, run smoke checks (uvicorn + curl repro), open a PR with summary and rationale.
- Runbook: Add a “Ticket creation fails” playbook describing repro, analysis, and resolution.

## Add Intelligence to CRM
- Read ticket descriptions and classify severity by adding intelligence to the existing CRM. This gives your CRM “thinking ability.”
- Implement a simple classifier via the SDK to infer severity from ticket descriptions (e.g., keywords → low/medium/high/critical).
- Use this to pre-fill severity or flag critical issues.

## What SDK agents can add
- Insight: AST-aware diffs and code context vs raw text search.
- Automation: Create PRs, request reviews, enforce CI checks.
- Consistency: Codify playbooks so future regressions are auto-diagnosed.
- Guidance: Inline prompts in IDE to guide devs toward safe fixes.
- Validation: Integrate smoke tests before proposing a PR.

## References
- Copilot SDK: https://github.com/github/copilot-sdk
- Build GitHub Copilot Extensions: https://docs.github.com/en/copilot/building-copilot-extensions
- FastAPI Testing: https://fastapi.tiangolo.com/advanced/testing/
- Pydantic v2 Models: https://docs.pydantic.dev/latest/
