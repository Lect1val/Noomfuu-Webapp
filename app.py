from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('user_profile.html')


@app.route('/analytic')
def analytic():
    return render_template('feeling_analytic.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
