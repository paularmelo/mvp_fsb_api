from pydantic import BaseModel
from typing import Optional, List
from model.receita import Ingredientes


class IngredientesSchema(BaseModel):
    """ Define como um novo ingrediente a ser inserido deve ser representado
    """
    descricao: str = "Ovos"
    quantidade: int = 3
    unidade_medida: str = "Unidade"
    receita_id: str = "1"


class IngredienteBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do ingrediente.
    """
    descricao: str = "Ovos"


class ListagemIngredientesSchema(BaseModel):
    """ Define como uma listagem de ingredientes será retornada.
    """
    ingredientes: List[IngredientesSchema]


def apresenta_ingredientes(ingrediente: Ingredientes):
    """ Retorna uma representação da receita seguindo o schema definido em
        IngredienteViewSchema.
    """
    return {

    }


class IngredientesViewSchema(BaseModel):
    """ Define como um ingrediente será retornado: ingrediente + comentários.
    """
    descricao: str = "Ovos"
    quantidade: int = 3
    unidade_medida: str = "Unidade"
    receita_id: str = "1"


class IngredientesDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str
