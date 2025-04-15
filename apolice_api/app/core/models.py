from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Parcela(Base):
    __tablename__ = "parcela"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer)
    valor = Column(Float)
    produto = Column(Integer)

    # Relacionamento opcional com a tabela 'produto', se necessário
    # produto_id = Column(Integer, ForeignKey("produto.id"))

    # Se precisar de uma relação, você pode adicionar isso
    # produto = relationship("Produto", back_populates="parcelas")

    def __repr__(self):
        return f"<Parcela id={self.id} numero={self.numero} valor={self.valor} produto={self.produto}>"
