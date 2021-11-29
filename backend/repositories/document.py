from database import Database
from models import Document


class DocumentRepository:
    """
    documents repository for accessing document data
    """

    def __init__(self):
        self._database = Database

    async def get_all_async(self):
        query = Document.__table__.select()

        return self._database.iterate(query)
