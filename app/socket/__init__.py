from . import views, errors
from flask import Flask
from flask import render_template
from flask_socketio import SocketIO
from flask import render_template, url_for
from . import main
from flask_login import login_required, current_user


from flask import Blueprint
main = Blueprint('main', __name__)

app = Flask(__name__)
socketio = SocketIO(app)


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
