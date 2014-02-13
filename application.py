from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/docs')
def docs():
    return render_template('docs.html', docs=True)

@app.route('/challenge')
def challenge():
    return render_template('challenge.html', challenge=True)

@app.route('/about')
def about():
    return render_template('about.html', about=True)

@app.route('/contact')
def contact():
    return render_template('contact.html', contact=True)

if __name__ == '__main__':
    app.debug = True
    app.run()
