from fastmcp import FastMCP
from court_listener import CourtListener
from typing import Optional, List, Dict, Any

mcp = FastMCP(
    name="Court Listener MCP",
    instructions="MCP server for performing legal research via the CourtListener API."
)

# Initialize the client (will use COURTLISTENER_API_TOKEN from .env)
# The client will be instantiated on demand or globally.
# For simplicity, we'll instantiate it inside each tool or globally if token is present.

def get_client():
    return CourtListener()

@mcp.tool()
async def search_legal_records(
    q: str, 
    court: Optional[str] = None, 
    type: Optional[str] = None, 
    date_filed: Optional[str] = None
) -> Dict[str, Any]:
    """
    Search CourtListener records (opinions, dockets, etc.).
    
    Args:
        q: Query string (keywords, case name, etc.)
        court: Optional court filter (e.g., 'scotus')
        type: Optional type filter ('opinions' or 'dockets')
        date_filed: Optional date filed filter (e.g., '2023-01-01' or range)
    """
    client = get_client()
    return await client.search(q, court=court, type=type, date_filed=date_filed)

@mcp.tool()
async def get_opinion(opinion_id: int) -> Dict[str, Any]:
    """
    Retrieve the full text and metadata of a specific opinion.
    """
    client = get_client()
    return await client.get_opinion(opinion_id)

@mcp.tool()
async def get_cluster(cluster_id: int) -> Dict[str, Any]:
    """
    Retrieve cluster details (lists opinions in a case).
    """
    client = get_client()
    return await client.get_cluster(cluster_id)

@mcp.tool()
async def get_docket(docket_id: int) -> Dict[str, Any]:
    """
    Retrieve docket metadata (date filed, parties, etc.).
    """
    client = get_client()
    return await client.get_docket(docket_id)

@mcp.tool()
async def list_courts(q: Optional[str] = None) -> Dict[str, Any]:
    """
    List or search for courts to find their abbreviations/IDs.
    """
    client = get_client()
    return await client.list_courts(q)

@mcp.tool()
async def verify_citations(text: str) -> List[Dict[str, Any]]:
    """
    Verify legal citations in a block of text and prevent hallucinations.
    """
    client = get_client()
    return await client.verify_citations(text)

if __name__ == "__main__":
    mcp.run()
