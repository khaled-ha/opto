from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, func


class Base:
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    deleted_at = Column(DateTime(timezone=True), nullable=True)


Base = declarative_base(cls=Base)
