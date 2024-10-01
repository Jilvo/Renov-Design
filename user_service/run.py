from app.create_app import create_app
from asgiref.wsgi import WsgiToAsgi

app = create_app()
asgi_app = WsgiToAsgi(app)
if __name__ == "__main__":
    app.run(port=5000, debug=True)
