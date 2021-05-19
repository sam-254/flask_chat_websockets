from flask import Flask
from flask import Flask, render_template, session, copy_current_request_context

from flask_socketio import SocketIO, send

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio_ = SocketIO(app, cors_allowed_origins='*', async_mode=async_mode)


@socketio_.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio_.async_mode)


if __name__ == '__main__':
    socketio_.run(app, debug=True)
