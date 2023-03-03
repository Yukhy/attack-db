from sqlalchemy import Column, Integer, String, Text
from settings import Engine, Base, Session

class Tactic(Base):
    __tablename__ = "tactic"
    id = Column(Integer, primary_key=True)
    external_id = Column(String(6), unique=True, nullable=False)
    name = Column(String(255))
    description = Column(Text())

    def __init__(self):
        Tactic.metadata.create_all(bind=Engine)

    # ta_idをKey, idをValueとした辞書を返す
    def get_id_pair_dict(self):
        lst = Session.query(Tactic.id, Tactic.ta_id).all()
        dic = {el[1]: el[0] for el in lst}
        return dic
    
    def get_id_by_name(name :str):
        return Session.query(Tactic).filter(Tactic.name == name).first().id