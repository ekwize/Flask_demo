from flask import Flask, request, render_template, flash, url_for

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}

app.config['SECRET_KEY'] = 'zxcvbnm0501'
app.config['MAX_CONTENT_LENGTH'] = 8 * 10 * 1024 * 1024

menu = [{'name':'Главная', 'url':'/'},
        {'name':'Регистрация', 'url':'/form'}]

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

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html', menu=menu), 404
            
if __name__ == '__main__': 
    app.run(debug = True)



    