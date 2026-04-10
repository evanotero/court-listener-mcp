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
- **Legal Research Skill**: A specialized persona and workflow for senior legal researchers to discover, analyze, and verify legal precedents.

## Setup

### 1. Requirements

- Python 3.10+
- [Gemini CLI](https://gemini.google.com/)
- CourtListener API Token (Sign up at [CourtListener](https://www.courtlistener.com/api/))

### 2. Configure MCP Server

1. Navigate to the `server/` directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your API token:
   ```bash
   COURTLISTENER_API_TOKEN=your_token_here
   ```

### 3. Install the Skill

Install the legal research skill to your workspace:
```bash
gemini skills install legal-research.skill --scope workspace
```

### 4. Usage

1. Reload your skills in an interactive Gemini session:
   ```bash
   /skills reload
   ```
2. Start researching:
   - "Search for recent student loan forgiveness cases in SCOTUS."
   - "Summarize the majority opinion in 576 U.S. 644 and verify the citations."

## Project Structure

- `server/`: Python FastMCP server implementation.
- `skills/`: Source code for the Legal Research skill.
- `legal-research.skill`: Packaged skill for installation.
- `.spec/`: CourtListener API documentation and specifications.

## Support

This project is powered by [Free Law Project](https://free.law). Please consider supporting their mission to make legal data open and accessible.
