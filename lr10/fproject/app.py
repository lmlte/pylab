from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from create_db import db
from models import Song

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение и экземпляр SQLAlchemy
db.init_app(app)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/songs')
def songs():
	songs_list = Song.query.all()
	return render_template('songs.html', songs=songs_list)

@app.route('/blog')
def blog():
	return 'Это блог с заметками о работе и увлечениях.'

@app.route('/user/<int:user_id>')
def user_profile(user_id):
	return f"Это профиль пользователя с ID {user_id}"

@app.route('/user/<username>')
def user_profile2(username):
	return f"Это профиль пользователя {username}"

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		# проверка логина и пароля
		return 'Вы вошли в систему!'
	else:
		return render_template('login.html')

if __name__ == '__main__':
	app.run(port=80, debug=True)