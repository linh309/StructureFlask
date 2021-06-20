import os

from flask import Flask, current_app

def create_app(config = None):
    app = Flask(__name__)
    app.config.from_object('config')

    from app.auth import auth_controller
    app.register_blueprint(auth_controller.bp)

    from app.admin.question import question_controller
    app.register_blueprint(question_controller.bp)

    @app.route('/up')
    def Up():
        return f"Up {current_app.config['DATABASE']}"

    

    return app