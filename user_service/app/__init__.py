from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
app.config.from_object("config.Config")
swagger = Swagger(app)


from app import views
