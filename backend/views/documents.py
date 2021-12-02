from starlette.endpoints import HTTPEndpoint
from starlette.responses import JSONResponse

from repositories import DocumentRepository
from models import Document


class Documents(HTTPEndpoint):
    """
    Fetch Documents as JSON
    """

    repository = DocumentRepository()

    async def get(self, request):
        result = await self.repository.get_all_async()

        docs = [
            {
                "title": document["title"],
                "position": document["position"],
                "type": document["type"],
                "id": document["id"],
            }
            async for document in result
        ]
        return JSONResponse(docs)

    async def post(self, request):
        data = await request.json()

        result = await self.repository.add_async(data)

        return JSONResponse(data)
