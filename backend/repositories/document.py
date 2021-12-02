from database import Database
from models import Document


class DocumentRepository:
    """
    documents repository for accessing document data
    """

    def __init__(self):
        self._database = Database
        self._table = Document.__table__

    async def get_all_async(self):
        query = self._table.select()

        return self._database.iterate(query)

    async def add_async(self, value):
        query = self._table.insert()

        return await self._database.execute(query, values=value)
