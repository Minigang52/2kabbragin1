from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Игра сохраняется в глобальной переменной
game_state = {
    'board': [''] * 9,
    'current_player': 'X',
    'game_active': True,
    'winner': None,
    'nickname': ''
}

@app.route('/')
def index():
    return render_template('index.html', game=game_state)

@app.route('/move', methods=['POST'])
def move():
    index = int(request.json['index'])
    nickname = request.json.get('nickname', '').strip()

    if not nickname:
        return jsonify({'status': 'error', 'message': 'Введите никнейм'}), 400

    if not game_state['game_active']:
        return jsonify({'status': 'error', 'message': 'Игра завершена'}), 400

    if game_state['board'][index] != '':
        return jsonify({'status': 'error', 'message': 'Эта клетка занята'}), 400

    game_state['board'][index] = game_state['current_player']

    # Проверка победителя
    if check_win(game_state['board']):
        game_state['winner'] = game_state['current_player']
        game_state['game_active'] = False
        message = f"Победили {('крестики' if game_state['winner']=='X' else 'нолики')}"
        return jsonify({'status': 'win', 'message': message, 'board': game_state['board']})

    # Проверка ничьи
    if '' not in game_state['board']:
        game_state['game_active'] = False
        return jsonify({'status': 'draw', 'message': 'Ничья!', 'board': game_state['board']})

    # Меняем ход
    game_state['current_player'] = 'O' if game_state['current_player'] == 'X' else 'X'
    return jsonify({'status': 'continue', 'board': game_state['board'], 'next_player': game_state['current_player']})

@app.route('/reset', methods=['POST'])
def reset():
    game_state['board'] = [''] * 9
    game_state['current_player'] = 'X'
    game_state['game_active'] = True
    game_state['winner'] = None
    return jsonify({'status': 'reset'})

def check_win(board):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],  # строки
        [0,3,6], [1,4,7], [2,5,8],  # столбцы
        [0,4,8], [2,4,6]            # диагонали
    ]
    for combo in wins:
        a, b, c = combo
        if board[a] != '' and board[a] == board[b] == board[c]:
            return True
    return False

if __name__ == '__main__':
    app.run(debug=True, port=5005)