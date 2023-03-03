from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from settings import Engine, Base

class Command(Base):
    __tablename__ = "command"
    id = Column(Integer, primary_key=True)
    command = Column(Text())
    technique_id = Column(ForeignKey('technique.id',onupdate='CASCADE', ondelete='CASCADE'))
    
    def __init__(self):
        Command.metadata.create_all(bind=Engine)