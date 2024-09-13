from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
SQLALCHEMY_DATABASE_URL = "postgresql://tomfyfe@localhost:5432/calm_plan"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()