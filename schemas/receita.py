from pydantic import BaseModel
from typing import Optional, List
from model.receita import Receita
from model.ingredientes import Ingredientes

from schemas import IngredientesSchema


class ReceitaSchema(BaseModel):
    """ Define como receita a ser inserida deve ser representada
    """
    titulo: str = "Bolo de Chocolate"
    status: str = "Aprovado"
    preparo: str = "Misture todos os ingredientes..."
    categoria: str = "Doce"
    ingredientes: List[IngredientesSchema]


class ReceitaBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no título da receita
    """
    id: int = 1
    titulo: str = "Bolo"


class ListagemReceitasSchema(BaseModel):
    """ Define como uma listagem de receitas será retornada.
    """
    receitas: List[ReceitaSchema]


def apresenta_receitas(receitas: List[Receita]):
    """ Retorna uma representação da receita seguindo o schema definido em
        ReceitaViewSchema.
    """
    result = []
    for receita in receitas:
        result.append({
            "id": receita.id,
            "titulo": receita.titulo,
            "status": receita.status,
            "categoria": receita.categoria,
            "preparo": receita.preparo,
        })

    return {"receitas": result}


class ReceitaViewSchema(BaseModel):
    """ Define como a receita será retornada: receita + ingredientes.
    """
    id: int = 1
    titulo: str = "Bolo de Chocolate"
    status: str = "Aprovado"
    preparo: str = "Misture todos os ingredientes..."
    categoria: str = "Doce"
    ingredientes_lista: List[IngredientesSchema]


class ReceitaDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str


def apresenta_receita(receita: Receita):
    """ Retorna uma representação da Receita seguindo o schema definido em
        ReceitaViewSchema.
    """
    return {
        "id": receita.id,
        "titulo": receita.titulo,
        "status": receita.status,
        "categoria": receita.categoria,
        "preparo": receita.preparo,
        "ingredientes": [{"id": c.id,
                          "descricao": c.descricao,
                          "quantidade": c.quantidade,
                          "unidade_medida": c.unidade_medida
                          } for c in receita.ingredientes_lista]

    }
