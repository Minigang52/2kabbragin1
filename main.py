import logging
from doctest import debug
from logging.handlers import RotatingFileHandler
from flask import Flask,jsonify, redirect, request, url_for
from flasgger import Swagger, LazyString, LazyJSONEncoder, swag_from

app = Flask(__name__)
import json
def load():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        print(data)
        return data
def dump():
    with open('data.json', 'w') as json_file:
        json.dump(json_file)
        return 1

app.json_encoder = LazyJSONEncoder

app.logger.setLevel(logging.INFO)

file_handler= RotatingFileHandler('app.log', maxBytes=1_000_000, backupCount=3)
file_handler.setFormatter(logging.Formatter("%(asctime)s [%levelname)s] %(name)s:%(message)"))

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter(
    "%(asctime)s [%levelname)s] %(name)s:%(message)"))

app.logger.addHandler(file_handler)
app.logger.addHandler(stream_handler)

@app.route("/", methods=['GET', "POST"])
def index():
    pass

@app.route("/registration", methods=['POST'])
def registration():
    app.logger.info("Регистрация")
    return jsonify({"message": "Регистрация"}), 201

@app.route("/login", methods=['POST'])
def login():
    app.logger.info("Вход в систему")
    return jsonify({"message": "Вход"}), 200

@app.route("/change-password", methods=['POST'])
def change_password():
    app.logger.info("Смена пароля")
    return jsonify({"message": "Пароль сменен"}), 200

@app.route("/delete-user", methods=['POST'])
def delete_user():
    app.logger.warning("Удаление пользователя")
    return jsonify({"message": "Пользователь удален"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
