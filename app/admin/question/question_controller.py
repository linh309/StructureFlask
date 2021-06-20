from flask import (
    Blueprint, render_template
)
prefix = "admin/question"
bp = Blueprint("question", __name__, url_prefix = f"/{prefix}")

@bp.route('/', methods=['GET'])
def index():
    return render_template(f'{prefix}/index.html')