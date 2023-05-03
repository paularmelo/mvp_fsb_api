from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from model import Base


class Ingredientes(Base):
    __tablename__ = 'ingredientes'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(40))
    quantidade = Column(Integer)
    unidade_medida = Column(String(20))

    # Definição do relacionamento entre o ingredientes e receita.
    # Aqui está sendo definido a coluna 'receita' que vai guardar
    # a referencia a receita, a chave estrangeira que relaciona
    # receita aos ingredientes.
    receita = Column(Integer, ForeignKey("receita.pk_receita"), nullable=False)

    def __init__(self, descricao: str, quantidade: Integer, unidade_medida: str, receita: str):
        """
        Cria um Ingrediente

        Arguments:
            decricao: nome do ingrediente.
            quantidade: quantidade do ingrediente para a receita
            unidadeMedida: unidade de medida do ingrediente
        """
        self.descricao = descricao
        self.quantidade = quantidade
        self.unidade_medida = unidade_medida
        self.receita = receita
