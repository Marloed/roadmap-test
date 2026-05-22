from piccolo.conf.apps import AppRegistry
from piccolo.engine.postgres import PostgresEngine
from dotenv import load_dotenv
import os

load_dotenv()

DB = PostgresEngine(

    config={
        "database": os.getenv("DATABASE_NAME"),
        "user": os.getenv("DATABASE_USER"),
        "host": os.getenv("DATABASE_HOST"),
        "port": int(os.getenv("DATABASE_PORT", "5432")),
    }
)

APP_REGISTRY = AppRegistry(
    apps=[
        "app.piccolo_app",
    ]
)
