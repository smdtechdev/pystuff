from tarfile import FIFOTYPE
from flask import request
from flask import Flask, flash, render_template, url_for

app = Flask(__name__)
app.secret_key = "12345"

@app.route('/')

def index():
    flash("What's your name?")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    
@app.route('/greet', methods=['POST'])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you")
    return render_template('index.html')