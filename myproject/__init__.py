from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
db=SQLAlchemy(app)



def createapp():
    app.config['SECRET_KEY']='thisiasecret'
    app.config['SQLALCHEMY_DATABSE_URI']='sqlite:///database.db'

    from .views import views 

    app.register_blueprint(views,url_prefix='/')

    db.init_app(app)
    db.create_all()
    return app

def createDB(app):
    print("database created")
