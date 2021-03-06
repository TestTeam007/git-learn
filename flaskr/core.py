from flask import Flask


def create_app():
    app = Flask(__name__)

    from .blueprints.public import routes
    app.register_blueprint(routes.bp)

    return app
