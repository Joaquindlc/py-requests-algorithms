from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    ALLOWED_ORIGINS: list[str] = ["http://localhost:5173"]

    #URLs de APIs externas
    DOLAR_API_URL: str
    ARGENTINA_DATOS_API_URL: str
    OPEN_LIBRARY_API_URL: str
    POKE_API_URL: str
    JIKAN_API_URL: str
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        
settings = Settings() 