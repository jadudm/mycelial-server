from flask import Blueprint


main = Blueprint('upload', __name__)


@main.route('/')
def index():
    return "upload"