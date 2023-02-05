from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from settings import Engine, Base, Session

class Technique(Base):
    __tablename__ = "technique"
    id = Column(Integer, primary_key=True)
    t_id = Column(String(5), unique=True)
    name = Column(String(255))
    description = Column(Text())

    def __init__(self):
        Technique.metadata.create_all(bind=Engine)
    
    # t_idをKey, idをValueとした辞書を返す
    def get_id_pair_dict(self):
        lst = Session.query(Technique.id, Technique.t_id).all()
        dic = {el[1]: el[0] for el in lst}
        return dic