from typing import ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeMeta

DBBaseModel: DeclarativeMeta = declarative_base()

class Settings(BaseSettings):
    """
    Configurações Gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:root@localhost:5432/faculdade'
    DBBaseModel: ClassVar = DBBaseModel

    class Config:
        case_sensitive = True


settings = Settings()