from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

lm = LoginManager()
lm.init_app(app)



        


from app.controllers import default
from app.models.tables import User
 

@lm.user_loader
def load_user(user_id):
    
    return User.query.get(int(user_id))