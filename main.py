from blacksheep import Application
from dotenv import load_dotenv

import app.misc_routes
import app.users_routes

load_dotenv()
app = Application()