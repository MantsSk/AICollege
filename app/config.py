from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # App
    secret_key: str = "dev-secret-change-me"
    app_name: str = "AI College"
    base_url: str = "http://localhost:8000"
    debug: bool = False
    allowed_hosts: str = "localhost,127.0.0.1,testserver"
    secure_ssl_redirect: bool = False

    # Database
    database_url: str = "postgresql+psycopg2://aicollege:aicollege@localhost:5432/aicollege"

    # AI Mentor
    ai_model: str = "gemini/gemini-1.5-flash"
    ai_temperature: float = 0.3
    ai_max_tokens: int = 1024
    mentor_max_message_chars: int = 4000
    ai_mentor_requires_subscription: bool = False
    gemini_api_key: str = ""
    openai_api_key: str = ""
    anthropic_api_key: str = ""

    # Limits
    free_daily_ai_messages: int = 5
    paid_daily_ai_messages: int = 200
    free_lessons_per_course: int = 2

    # Stripe
    payments_enabled: bool = False
    stripe_secret_key: str = ""
    stripe_publishable_key: str = ""
    stripe_webhook_secret: str = ""
    stripe_price_id: str = ""
    subscription_price_eur: float = 9.99

    @property
    def allowed_host_list(self) -> list[str]:
        return [host.strip() for host in self.allowed_hosts.split(",") if host.strip()]

    def validate_for_runtime(self) -> None:
        if not self.debug and self.secret_key in {"dev-secret-change-me", "dev-secret-do-not-use-in-production"}:
            raise RuntimeError("Set SECRET_KEY to a long random value before running with DEBUG=false.")
        if not self.debug and self.base_url.startswith("http://"):
            raise RuntimeError("Set BASE_URL to your public https:// URL before running with DEBUG=false.")
        if self.payments_enabled:
            required = {
                "STRIPE_SECRET_KEY": self.stripe_secret_key,
                "STRIPE_WEBHOOK_SECRET": self.stripe_webhook_secret,
                "STRIPE_PRICE_ID": self.stripe_price_id,
            }
            missing = [name for name, value in required.items() if not value]
            if missing:
                raise RuntimeError(
                    "Payments are enabled but Stripe is incomplete: " + ", ".join(missing)
                )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
