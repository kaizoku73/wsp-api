from flask import Flask
import config as c

def create_app():
    app = Flask(__name__)

    #load config and logging from config.py
    c.load_config(app)
    c.config_log()

    