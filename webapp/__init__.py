from flask import Flask
from webapp.start_page.views import blueprint as start_blueprint



def create_app():
    app = Flask(__name__)
    
    app.config.from_pyfile('config.py') 

    app.register_blueprint(start_blueprint)

    return app