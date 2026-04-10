# Legal Research AI

An extension for Gemini CLI to perform structured legal research using the [CourtListener](https://www.courtlistener.com/) API.

## Features

- **MCP Server (Python/FastMCP)**: Connects directly to the CourtListener REST v4 API.
  - `search_legal_records`: Find cases and dockets by keyword, party, or jurisdiction.
  - `get_opinion`: Retrieve full-text opinions with linked citations.
  - `get_cluster`: View case groupings and related decisions.
  - `get_docket`: Access case metadata, filing dates, and parties.
  - `list_courts`: Search for court abbreviations and IDs.
  - `verify_citations`: **Anti-hallucination guardrail** that validates legal citations against the CourtListener database.
- **Legal Research Skill**: A specialized persona and workflow for senior legal researchers to discover, analyze, and verify legal precedents. **Automatically discovered** after extension installation.

## Setup

### 1. Requirements

- [uv](https://docs.astral.sh/uv/) (required for the MCP server)
- [Gemini CLI](https://gemini.google.com/)
- CourtListener API Token (Sign up at [CourtListener](https://www.courtlistener.com/api/))

### 2. Installation

Install the extension by linking it to your local Gemini CLI environment:
```bash
gemini extensions link .
```
This will:
1.  **Register the MCP server**: `court-listener-mcp` will be available in all your sessions.
2.  **Auto-install the Skill**: The `legal-research` skill will be discovered and made available.

### 3. Configuration

You will be prompted for your **CourtListener API Key** during installation or the first time you use the extension. You can also set it manually:
```bash
export COURTLISTENER_API_TOKEN=your_token_here
```

## Usage

1.  Start an interactive Gemini session.
2.  Reload your skills if needed:
    ```bash
    /skills reload
    ```
3.  Start researching:
    - "Search for recent student loan forgiveness cases in SCOTUS."
    - "Summarize the majority opinion in 576 U.S. 644 and verify the citations."

## Project Structure

- `server/`: Python FastMCP server implementation.
- `skills/`: Source code for the Legal Research skill (auto-discovered).
- `gemini-extension.json`: Extension manifest defining the MCP server and settings.
- `.spec/`: CourtListener API documentation and specifications.

## Support

This project is powered by [Free Law Project](https://free.law). Please consider supporting their mission to make legal data open and accessible.
