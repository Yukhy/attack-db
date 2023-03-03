from sqlalchemy import Column, Integer, ForeignKey
from settings import Engine, Base

# TacticsとTechniquesの中間テーブル
class Reason(Base):
    __tablename__ = "reason"
    id = Column(Integer, primary_key=True)
    tactic_id = Column(ForeignKey('tactic.id',onupdate='CASCADE', ondelete='CASCADE'))
    technique_id = Column(ForeignKey('technique.id',onupdate='CASCADE', ondelete='CASCADE'))

    def __init__(self):
        Reason.metadata.create_all(bind=Engine)