from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.core.publisher import send_to_queue
from app.core.schemas import ApoliceInput

app = FastAPI()

@app.post("/emitir-apolice")
async def emitir_apolice(payload: ApoliceInput):
    try:
        # Envia para a fila apropriada com base no produto
        send_to_queue(payload.produto, payload.dict())
        return {"message": "Processamento iniciado."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
