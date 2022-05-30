from flask import Flask, render_template
from flask import redirect, url_for
from flask_dance.contrib.github import make_github_blueprint, github
import secrets
import os
import sqlite3

# from flask_mail import Mail, Message
#
# app = Flask(__name__)
#
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
# app.config['MAIL_PASSWORD'] = '*****'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
# mail = Mail(app)
#
#
# @app.route("/about")
# def about():
#     msg = Message('Hello', sender='yourId@gmail.com', recipients=['someone1@gmail.com'])
#     msg.body = "Hello Flask message sent from Flask-Mail"
#     mail.send(msg)
#     return "Sent"

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

github_blueprint = make_github_blueprint(client_id="73917df0ae61e5fc6c24", client_secret=
"8e0ea7029e0ffcf2cd4bc5c03cc217a0ed9ccbe2")
app.register_blueprint(github_blueprint, url_prefix='/login')


@app.route('/')
def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            return render_template('index.html')

    return '<h1>Request failed!</h1>'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return app.send_static_file('about.html')


@app.route('/gallery')
def gallery():
    return app.send_static_file('gallery.html')


@app.route('/guestbook', methods=('GET', 'POST'))
def guestbook():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('guestbook.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)
