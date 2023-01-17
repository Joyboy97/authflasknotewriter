
from flask import Flask
# this file makes website a python file that can be imported
from flask_sqlalchemy import SQLAlchemy
from os import path
db = SQLAlchemy()
DB_NAME ="database.db"

def create_app():
    app =Flask(__name__)
    app.config['SECRET_KEY']='geoife sdnvefeomewo' #incriptor
    app.config['SQLALCHEMY_DATABASE_URI']= f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') 

    from .models import User,Note
    
    with app.app_context():
        db.create_all()
     #make sure the file runs before anything is run
    
    return app
