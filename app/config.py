from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # App
    secret_key: str = "dev-secret-change-me"
    app_name: str = "AI College"
    base_url: str = "http://localhost:8000"
    debug: bool = True

    # Database
    database_url: str = "postgresql+psycopg2://aicollege:aicollege@localhost:5432/aicollege"

    # AI Mentor
    ai_model: str = "gemini/gemini-1.5-flash"
    ai_temperature: float = 0.3
    ai_max_tokens: int = 1024
    gemini_api_key: str = ""
    openai_api_key: str = ""
    anthropic_api_key: str = ""

    # Limits
    free_daily_ai_messages: int = 5
    paid_daily_ai_messages: int = 200
    free_lessons_per_course: int = 2

    # Stripe
    stripe_secret_key: str = ""
    stripe_publishable_key: str = ""
    stripe_webhook_secret: str = ""
    stripe_price_id: str = ""
    subscription_price_eur: int = 20


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
