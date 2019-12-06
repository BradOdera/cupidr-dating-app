from . import views, errors
from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask import render_template, url_for
from . import main
from flask_login import login_required, current_user
from flask import Blueprint
main = Blueprint('main', __name__)

