from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/ninjas/<collor>')
def difninja(collor):
    print collor
    return render_template("ninjerk.html", color=collor, phrase="hello")


app.run(debug=True)