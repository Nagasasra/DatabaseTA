from flask import Flask
from dotenv import load_dotenv
load_dotenv()
import os

from src.routers.auth import auth_url
from src.routers.people import people_url
from src.routers.menu import menu_url
from src.routers.trans import trans_url

app = Flask(__name__, template_folder="src/views")

app.register_blueprint(auth_url, url_prefix="")
app.register_blueprint(people_url, url_prefix="")
app.register_blueprint(menu_url, url_prefix="")
app.register_blueprint(trans_url, url_prefix="")

if __name__ == '__main__':
	app.secret_key = os.getenv("SECRETKEY")
	app.run(port=7000, debug=True)
	