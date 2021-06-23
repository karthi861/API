import logging
from flask import Flask
from config import CONFIG
from handlers.feed_handler import FEED
from handlers.authentication_handler import AUTHENTICATION
from models import db

logging.basicConfig(
    format='%(levelname)-8s %(asctime)s,%(msecs)d  [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.INFO
)


def init_app():
    app = Flask(__name__)
    app.secret_key = ['thisissecret']
    app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = CONFIG['SQLALCHEMY_TRACK_MODIFICATIONS']
    db.init_app(app)
    app.register_blueprint(FEED)
    app.register_blueprint(AUTHENTICATION)
    return app
