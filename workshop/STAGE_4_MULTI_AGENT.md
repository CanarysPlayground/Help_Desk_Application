# Stage 4: Multi‑Agent — Safety, boundaries, and flow

> **Related Exercises:** 
> - [All Exercises Index](exercises/INDEX.md)
> - [Exercise 1: Create Custom CLI Agent](exercises/EXERCISE_1_CLI_AGENT.md)
> - [Exercise 4: Self-Healing with SDK](exercises/EXERCISE_4_SELF_HEALING.md)

Goal: Show how CLI, SDK, and MCP agents collaborate safely, plus build a custom agent.

## How multi‑agent workflows emerge
- Triage (CLI agent): Quick repro via curl, rg for hotspots.
- Diagnosis (MCP agent): Structured route/schema/model mapping; DB inspection.
- Remediation (SDK agent): Propose minimal diffs; open PR; run smoke tests.
- Validation (CLI/MCP): HTTP probes + DB checks confirm resolution.

## Create a Custom Copilot Agent (CLI)
- Reference: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents
- Steps:
	- Use Copilot CLI to scaffold a custom coding agent.
	- Define capabilities (read workspace, propose diffs, run checks).
	- Configure delegates for specific tasks (e.g., severity classification).
	- Implement the feature using a delegate: when a new ticket is created, delegate infers severity and suggests updates.
	- Wire agent actions to PR creation and review.

## What CLI agents can improve
- Fast feedback: Repro scripts and logs.
- Breadth: Wide scan across files without deep coupling.
- Simplicity: Works anywhere, minimal setup.

## What SDK agents can add
- Contextual diffs: Safer, smaller patches aligned to code style.
- Governance: PR templates, reviewers, CI gates.
- Iteration: Learn from past fixes to preempt recurrences.

## Where MCP tools fit
- Tooling contract: Clear capabilities; agents can call them reliably.
- Orchestration: Sequence searches, DB reads, and HTTP probes.
- Observability: Capture traces of decisions and actions.

## How safety & boundaries apply
- Least privilege: Read-first; writes gated by human confirmation.
- Scoped access: Workspace-only tools; explicit whitelists for network/db.
- Transparency: Log all actions, show diffs, require approvals.
- Compliance: Align with org policies and Microsoft/GitHub content guidelines.

## Suggested exercise
1. Reproduce the issue via Stage 1.
2. Implement the schema fix in app/schemas/ticket.py (ticket_id → id).
3. Validate via Stage 1 repro and Stage 3 http_probe.
4. Package as a PR using Stage 2 SDK flow.
5. Create a custom agent via CLI and implement severity inference using a delegate.
