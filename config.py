import os
from dotenv import load_dotenv
import sys
import logging


load_dotenv()

def load_config(app):
    app.config["token"] = os.getenv("ACCESS_TOKEN")
    app.config["app_id"] = os.getenv("APP_ID")
    app.config["app_secret"] = os.getenv("APP_SECRET")
    app.config["version"] = os.getenv("VERSION")
    app.config["number_id"] = os.getenv("PHONE_NUMBER_ID")
    app.config["user"] = os.getenv("USER_NUMBER")
    app.config["verify_token"] = os.getenv("VERIFY_TOKEN")

def config_log():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        stream=sys.stdout
    )