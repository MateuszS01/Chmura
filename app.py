from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/about")
def about():
    msg = Message('Hello', sender='yourId@gmail.com', recipients=['someone1@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return app.send_static_file('about.html')


@app.route('/gallery')
def gallery():
    return app.send_static_file('gallery.html')


if __name__ == '__main__':
    app.run(debug=True)
