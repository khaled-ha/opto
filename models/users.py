import uuid
from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.dialects import postgresql
from models.base import Base


class User(Base):
    __tablename__ = 'users'

    # id = Column(postgresql.UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    id = Column(Integer, default=uuid.uuid4, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String(120), index=True, unique=True)
    is_active = Column(Boolean, default=False)
