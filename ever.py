"""
flash() -  на стороне сервера
get_flash_messeges() - в шаблоне 

flash() -> session -> get_flash_messeges() -> шаблон
"""
from flask import Flask, render_template, url_for, request, flash, abort, session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'rfrbrfhb;rfbb5g5;rfbh5;rbfrghbg5u4erherh4t5'

@app.route('/')
def begin():
    return f"""
ссылка на <a href="/base">базовую</a> страницу<br>
ссылка на <a href="/start">стартовую</a> страницу<br>
ссылка на <a href={url_for('index')}>index</a> страницу<br>
ссылка на <a href={url_for('form')}>страницу</a>"""

@app.route('/dase/index')
def index():
    username = 'Stolyarov'
    return render_template('index.html', username=username)


@app.route('/day-<num>')
def day(num):
    return render_template(f'day-{num}.html')


@app.route('/photo-<num>')
def photo(num):
    return render_template(f'photo-{num}.html')


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/start')
def start():
    return render_template(f'start.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        for user in users:
            if request.form['username'] == user['username']:
                if request.form['password'] == user['password']:
                    return redirect(f"/profile/{user['username']}")
                else:
                    flash('Неправильный пароль', category='error')
                    break
            else:
                flash('Неправильный логин', category='error')


@app.route('/form',methods={'GET', 'POST'})
def form():
    if request.method == 'POST':
        if len(request.form[fullname]) < 5 and not request.form[fullname].isalpha():
            flash('Ошибка в имени. сообщение не отправлено!')
    else:
      flash('сообщение принято!')
      for iten in request.form:
        print(item, request.form[item])
    return render_template('form.html')

@app.route('/profile/<username>')
def profile(username):
    for user in users:
        if user['username'] == username:
            if 'logged_in' in session:
                if session['logged_in'] == username:
                    return render_template('profile.html', username=username)
        flash('Вам туда нельзя. Залогинтесь', category='error')
        return redirect(url_for('login'))

        abort(404)

if __name__ == '__main__':
    app.run(debug=True)



