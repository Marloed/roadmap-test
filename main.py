from blacksheep import Application
from dotenv import load_dotenv

import app.misc_routes
import app.users.users_routes
import app.devices.devices_routes

load_dotenv()
app = Application()