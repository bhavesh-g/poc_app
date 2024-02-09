from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)

socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
  return render_template('index.html')

@socketio.on('send notification')
def handle_notification(data):
  socketio.emit('receive_notification', data)
  print(data)

if __name__ == '__main__':
  socketio.run(app, allow_unsafe_werkzeug=True)

