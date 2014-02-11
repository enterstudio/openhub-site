from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/msr')
def msr():
    return render_template('msr.html', msr=True)

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
