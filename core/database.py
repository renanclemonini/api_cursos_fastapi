from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

from core.configs import settings

# Criação do engine assíncrono
engine: AsyncEngine = create_async_engine(settings.DB_URL)

# Configurando o sessionmaker para criar sessões assíncronas
Session: sessionmaker[AsyncSession] = sessionmaker(
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)
