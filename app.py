from flask import Flask, render_template

app = Flask(__name__)


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
