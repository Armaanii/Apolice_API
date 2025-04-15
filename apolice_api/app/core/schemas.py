from pydantic import BaseModel, Field, validator
from typing import Optional

# ---------------------- PRODUTO 111 ----------------------
class Endereco(BaseModel):
    rua: str
    numero: int

class Inquilino(BaseModel):
    nome: str
    CPF: str = Field(..., min_length=11, max_length=11)

class Beneficiario(BaseModel):
    nome: str
    CNPJ: str = Field(..., min_length=14, max_length=14)

class ItemProduto111(BaseModel):
    endereco: Endereco
    inquilino: Inquilino
    beneficiario: Beneficiario

class Valores(BaseModel):
    precoTotal: float
    parcelas: int

class Produto111(BaseModel):
    produto: int
    item: ItemProduto111
    valores: Valores

    @validator('produto')
    def validar_produto(cls, v):
        if v != 111:
            raise ValueError('Produto inválido para schema Produto111')
        return v

# ---------------------- PRODUTO 222 ----------------------
class ItemProduto222(BaseModel):
    placa: str = Field(..., min_length=7, max_length=7)
    chassi: str
    modelo: str

class Produto222(BaseModel):
    produto: int
    item: ItemProduto222
    valores: Valores

    @validator('produto')
    def validar_produto(cls, v):
        if v != 222:
            raise ValueError('Produto inválido para schema Produto222')
        return v
