from flask import (
    Blueprint, render_template
)
bp = Blueprint("auth",__name__, url_prefix="/auth")

@bp.route('/login', methods=('GET','POST'))
def login():
    return render_template('auth/login.html')


@bp.route('/logout', methods=('GET','POST'))
def logout():
    return "Logout"

@bp.route('/register', methods=('GET','POST'))
def register():
    return "Register"