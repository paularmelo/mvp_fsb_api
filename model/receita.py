from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from model import Base, Ingredientes


class Receita(Base):
    __tablename__ = 'receita'

    id = Column("pk_receita", Integer, primary_key=True)
    titulo = Column(String(140))
    categoria = Column(String(40))
    status = Column(String(40))
    preparo = Column(String(4000))

    data_insercao = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o receita e ingredientes
    ingredientes_lista = relationship("Ingredientes")

    def __init__(self, titulo: str, categoria: str, status: str, preparo: str,
                 data_insercao: Union[DateTime, None] = None):
        """
        Cria uma receita

        Arguments:
            titulo: titulo da receita.
            status: status da receita(Aprovada, Reprovada, Não testada)
            preparo: decrição do modo de fazer
            categoria: categoria da receita(Massas, doce, salgado, ligth)
            data_insercao: data de quando o produto foi inserido à base
        """
        self.titulo = titulo
        self.status = status
        self.preparo = preparo
        self.categoria = categoria

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_ingredientes(self, ingrediente: Ingredientes):
        """ Adiciona ingredientes a receita
        """
        self.ingredientes_lista.append(ingrediente)
