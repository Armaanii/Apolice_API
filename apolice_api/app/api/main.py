from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.core.schemas import Produto111, Produto222

app = FastAPI()

@app.post("/emitir")
def emitir_apolice(payload: dict):
    produto = payload.get("produto")

    if produto == 111:
        try:
            Produto111(**payload)
            return {"message": "Produto 111 validado com sucesso"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    elif produto == 222:
        try:
            Produto222(**payload)
            return {"message": "Produto 222 validado com sucesso"}
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    else:
        raise HTTPException(status_code=400, detail="Produto não suportado")
