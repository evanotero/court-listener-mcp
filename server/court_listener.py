import os
import httpx
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv

load_dotenv()

class CourtListener:
    BASE_URL = "https://www.courtlistener.com/api/rest/v4"

    def __init__(self, token: Optional[str] = None):
        self.token = token or os.getenv("COURTLISTENER_API_TOKEN")
        if not self.token:
            raise ValueError("COURTLISTENER_API_TOKEN must be set")
        
        self.headers = {
            "Authorization": f"Token {self.token}",
            "Accept": "application/json"
        }

    async def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.BASE_URL}/{endpoint.lstrip('/')}"
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()

    async def _post(self, endpoint: str, data: Optional[Dict[str, Any]] = None) -> Any:
        url = f"{self.BASE_URL}/{endpoint.lstrip('/')}"
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=self.headers, data=data)
            response.raise_for_status()
            return response.json()

    async def search(self, q: str, court: Optional[str] = None, type: Optional[str] = None, date_filed: Optional[str] = None) -> Dict[str, Any]:
        params = {"q": q}
        if court:
            params["court"] = court
        if type:
            params["type"] = type
        if date_filed:
            params["date_filed"] = date_filed
        return await self._get("search/", params=params)

    async def get_opinion(self, opinion_id: int) -> Dict[str, Any]:
        return await self._get(f"opinions/{opinion_id}/")

    async def get_cluster(self, cluster_id: int) -> Dict[str, Any]:
        return await self._get(f"clusters/{cluster_id}/")

    async def get_docket(self, docket_id: int) -> Dict[str, Any]:
        return await self._get(f"dockets/{docket_id}/")

    async def list_courts(self, q: Optional[str] = None) -> Dict[str, Any]:
        params = {}
        if q:
            params["full_name__icontains"] = q
        return await self._get("courts/", params=params)

    async def verify_citations(self, text: str) -> List[Dict[str, Any]]:
        return await self._post("citation-lookup/", data={"text": text})
