# Stage 3: MCP & Agents — Tool-aware orchestration

> **Related Exercise:** [Exercise 3: Build GitHub Actions Workflow](exercises/EXERCISE_3_BUILD_WORKFLOW.md)

Goal: Use Model Context Protocol (MCP) to expose repo tools to agents and orchestrate analysis + fixes.

> We use MCP tools when the CRM must take system-level actions.

## Steps
- Design tools (MCP server): `code_search` (ripgrep-like), `route_map` (FastAPI routes → schemas → models), `db_inspect` (SQLite schema/data), `http_probe` (GET/POST to dev server).
- Server: Implement an MCP server exposing these tools.
- Connect: Configure your agent client to talk to the MCP server.
- Workflow:
  1. Agent calls `route_map` → finds `TicketResponse.ticket_id`.
  2. Agent calls `code_search` → confirms mismatch vs `id`.
  3. Agent calls `db_inspect` → sees committed rows despite 500/422.
  4. Agent drafts patch and asks human to approve/apply.
  5. Agent runs `http_probe` post-fix to validate.
- Safety:
  - Tools are read-mostly; write actions require explicit confirmation.
  - Scope to workspace; no external network unless whitelisted.

## ✔ MCP Tools Use Cases in Your CRM

### Using GitHub MCP
- Create an issue when a critical ticket is submitted.

### GitHub MCP configuration
- Server repo: https://github.com/github/github-mcp-server
- Steps:
  - Clone and install the GitHub MCP server.
  - Configure authentication (GitHub token/permissions per README).
  - Define a tool (e.g., `create_issue`) bound to your repo.
  - From the CRM, invoke MCP client → call `create_issue` when `severity == "critical"`.
  - Log MCP calls and responses for observability.

## Where MCP tools fit
- Structured access: Standardize how agents call workspace tools.
- Composability: Chain code search, analysis, DB reads, and HTTP probes.
- Auditability: Log tool calls, inputs, and outputs for review.

## References
- Model Context Protocol Overview: https://modelcontextprotocol.org/
- MCP Python SDK & templates: https://github.com/modelcontextprotocol
- GitHub MCP Server: https://github.com/github/github-mcp-server
- FastAPI Routing: https://fastapi.tiangolo.com/tutorial/path-operation-functions/
