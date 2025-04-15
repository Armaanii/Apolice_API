from app.core.database import engine
from app.core.models import Base

def init():
    print("Criando as tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso.")

if __name__ == "__main__":
    init()
