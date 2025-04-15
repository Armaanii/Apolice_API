from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração do banco de dados PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgres_db:5432/apolice"

# Criação do engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)

# Sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para as classes
Base = declarative_base()