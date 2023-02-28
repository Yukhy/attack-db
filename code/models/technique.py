from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from settings import Engine, Base, Session

class Technique(Base):
    __tablename__ = "technique"
    id = Column(Integer, primary_key=True)
    sub_id = Column(Integer, primary_key=True)
    name = Column(String(255))
    description = Column(Text())

    def __init__(self):
        Technique.metadata.create_all(bind=Engine)