from blacksheep import Application
from dotenv import load_dotenv
import os

import app.misc_routes
import app.users_routes

load_dotenv()

database_url = os.getenv("DATABASE_URL")

app = Application()