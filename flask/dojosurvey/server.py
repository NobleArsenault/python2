from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results", methods=['POST'])
def results():
    location = request.form.get('location')
    favorite_language = request.form.get('favorite_language')
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    message = request.form.get("message")
    print request.form
    return render_template('results.html', location=location, favorite_language=favorite_language, firstname=firstname, lastname=lastname, message=message)


app.run(debug=True)