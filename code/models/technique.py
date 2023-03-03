from sqlalchemy import Column, Integer, String, Text,Boolean
from settings import Engine, Base, Session

class Technique(Base):
    __tablename__ = "technique"
    id = Column(Integer, primary_key=True)
    external_id = Column(String(9), unique=True, nullable=False)
    name = Column(String(255))
    description = Column(Text())
    is_subtechnique = Column(Boolean)

    def __init__(self):
        Technique.metadata.create_all(bind=Engine)

    def get_id_by_name(name :str):
        return Session.query(Technique).filter(Technique.name == name).first().id
    
    def get_id_by_external_id(external_id: str):
        return Session.query(Technique).filter(Technique.external_id == external_id).first().id
