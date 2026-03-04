from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    database_url: str = "postgresql://postgres.diglyrhbzpdcnlcimdiz:/v/Ht8gdAb6j_ek@aws-1-ap-south-1.pooler.supabase.com:5432/postgres"
    secret_key: str = "change_this_to_a_long_random_secret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60


settings = Settings()
