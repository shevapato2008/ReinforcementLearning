from flask import Flask, render_template
from flask_socketio import SocketIO
from src.game_session import GameSession

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

game_sessions = {}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect(auth):
    from flask import request
    sid = request.sid
    print(f'Client connected: {sid}')
    game = GameSession()
    game_sessions[sid] = {
        'game': game,
        'active': True
    }
    socketio.start_background_task(game_loop, sid)

def game_loop(sid):
    game_info = game_sessions.get(sid)
    if not game_info:
        return
    game = game_info['game']
    while game_info['active']:
        frame, done = game.advance()
        socketio.emit('frame', {'image': frame}, to=sid)
        if done:
            socketio.emit('game_over', to=sid)
        socketio.sleep(0.04) # ~25 FPS

@socketio.on('input')
def handle_input(data):
    from flask import request
    sid = request.sid
    game_info = game_sessions.get(sid)
    if game_info:
        game_info['game'].set_action(data.get('key'))

@socketio.on('restart')
def handle_restart():
    from flask import request
    sid = request.sid
    game_info = game_sessions.get(sid)
    if game_info:
        game_info['game'].reset()

@socketio.on('disconnect')
def handle_disconnect():
    from flask import request
    sid = request.sid
    print(f'Client disconnected: {sid}')
    game_info = game_sessions.pop(sid, None)
    if game_info:
        game_info['active'] = False
        game_info['game'].close()

if __name__ == '__main__':
    socketio.run(app, debug=True)
