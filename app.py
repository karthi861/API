from models import db
from flask_migrate import Migrate
from init import init_app
app = init_app()


migrate = Migrate(app, db)



@app.route('/')
def welcome():
    return "Welcome"


if __name__ == '__main__':
    app.run(debug=True)

