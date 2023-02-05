from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, UniqueConstraint
from settings import Engine, Base, Session

class Subtechnique(Base):
    __tablename__ = "subtechnique"
    __table_args__ = (UniqueConstraint('st_id','technique_id'),{})
    id = Column(Integer, primary_key=True)
    st_id = Column(String(3))
    name = Column(String(255))
    description = Column(Text())
    technique_id = Column(ForeignKey('technique.id',onupdate='CASCADE', ondelete='CASCADE'))

    def __init__(self):
        Subtechnique.metadata.create_all(bind=Engine)

    # st_idをKey, idをValueとした辞書を返す
    def get_id_pair_dict(self):
        lst = Session.query(Subtechnique.id, Subtechnique.st_id, Subtechnique.technique_id).all()
        dic = {(el[1], el[2]): el[0] for el in lst}
        return dic