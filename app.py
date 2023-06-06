from flask import Flask, request, render_template, flash, url_for, session, redirect

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

app.config['SECRET_KEY'] = 'zxcvbnm0501'
app.config['MAX_CONTENT_LENGTH'] = 8 * 10 * 1024 * 1024

menu = [{'name':'Главная', 'url':'/'},
        {'name':'Обратная связь', 'url':'/form'},
        {'name':'Авторизация', 'url':'/login'}]

@app.route("/")
def index():
    return render_template('index.html', title = 'ekwize', menu=menu)

@app.route("/form", methods = ['POST', 'GET'])
def page_form():
    if request.method == 'POST':
        if len(request.form['email']) >= 4:
            flash('Сообщение отправлено')
        else:
            flash('Ошибка отправки')
    return render_template('form.html', title = 'Загрузки', menu=menu)
@app.route("/login", methods=['POST', 'GET'])
def page_login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.form['username'] == "ekwize" and request.form['psw'] == "segaPRO2008":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=menu)




@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', title = 'Страница не найдена', menu=menu), 404
            
if __name__ == '__main__': 
    app.run(debug = True)



    