from flask import Flask, session, render_template, request, redirect, url_for,session
from datetime import datetime
import threading

app=Flask(__name__)
app.secret_key = 'ddddd'
user_connect = {}
users_thr = threading.Lock()

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('username')
        session['username']=user_name

        with users_thr:
            user_connect[session['username']] = {
                'login_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'ip': request.remote_addr
            }
        return redirect(url_for('dashboard'))
    return  render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard.html',
                           username=session['username'],
                           users=user_connect)

@app.route('/log_out')
def log_out():
    pass

@app.route('/game',  methods=['GET','POST'])
def game():
    return render_template('game.html')


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5006)