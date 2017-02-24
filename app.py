# app.py
import os, flask, flask_socketio

app = flask.Flask(__name__)
socketio = flask_socketio.SocketIO(app)

@app.route('/')
def hello():
    return 'Hello, world!'

@socketio.on('new massage')
def on_new_massage(data):
    socketio.emit('server sends data back', {
        'from server': data
    })

@socketio.on('connect')
def on_connect():
    potato()

def potato():
    socketio.emit('server says hello', {
        'message': 'Hello, client!'
    })

if __name__ == '__main__':
    socketio.run(
        app,
        host=os.getenv('IP', '0.0.0.0'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )

