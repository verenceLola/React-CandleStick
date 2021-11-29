from sqlalchemy import String, Column, Integer
from .base import Base
import sqlalchemy


class Document(Base):
    """
    document model definition
    """

    __tablename__ = "document"

    id = Column(Integer, primary_key=True)
    title = Column(String(length=50))
    position = Column(Integer)
    type = Column(String(30))
