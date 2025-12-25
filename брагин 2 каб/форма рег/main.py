from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        repeat_password = request.form.get('repeat_password')
        fullname = request.form.get('fullname')
        address = request.form.get('address')

        if password != repeat_password:
            return 'Пароли не совпадают!'

        print('Новая регистрация:')
        print(f'Email: {email}')
        print(f'Пароль: {password}')
        print(f'ФИО: {fullname}')
        print(f'Адрес: {address}')

        return 'Данные успешно отправлены!'
    return render_template('forma.html')

if __name__ == '__main__':
    app.run(debug=True)