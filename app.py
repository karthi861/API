from init import init_app
from models import db
from flask_migrate import Migrate
from flask import app
from flask import Flask
from config import CONFIG
from handlers.feed_handler import FEED



migrate = Migrate(app, db)



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = CONFIG['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = CONFIG['SQLALCHEMY_TRACK_MODIFICATIONS']
db.init_app(app)
app.register_blueprint(FEED)


@app.route('/')
def welcome():
    return "Welcome"

if __name__ == '__main__':
    app.run(debug=True)

