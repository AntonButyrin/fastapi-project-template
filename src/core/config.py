from pydantic import BaseSettings


class AdminSettings(BaseSettings):
    username: str
    password: str

    class Config:
        env_file = ".env"


class DatebaseSettings(BaseSettings):
    db_host: str
    db_port: str
    db_name: str
    db_user: str
    db_pass: str

    class Config:
        env_file = ".env"


class HostSettings(BaseSettings):
    allowed_host: str

    class Config:
        env_file = ".env"


datebase_settings = DatebaseSettings()
admin_settings = AdminSettings()
host_settings = HostSettings()


database_url = f"postgresql+asyncpg://{datebase_settings.db_user}:{datebase_settings.db_pass}@{datebase_settings.db_host}:{datebase_settings.db_port}/{datebase_settings.db_name}"
