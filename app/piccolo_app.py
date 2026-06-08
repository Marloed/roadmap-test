from piccolo.conf.apps import AppConfig
from .tables import User, Device

APP_CONFIG = AppConfig(
    app_name="app",
    migrations_folder_path="app/piccolo_migrations",
    table_classes=[User, Device],
)