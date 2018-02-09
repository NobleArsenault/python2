from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 1
    else:
        session["count"] += 1
    return render_template('index.html')

@app.route("/add2")
def add2():
    session["count"] += 1
    return redirect("/")

@app.route("/clear")
def clear():
    #session["count"] = 0
    session.clear()
    return redirect("/")

app.run(debug=True)




# if "count" not in session:
#     session["count"] = 1
# else:
#     session["count"] += 1
# return render_template('index.html')


# @app.route("/add2")
# def add2():
#     session["count"] += 1
# return redirect("/")

# @app.route("/clear")
# def clear():
#     #session["count"] = 0
#     session.clear()
# return redirect("/")


    #session is the dictionary count is the key and 1 is whats stored in the key
#     session['count'] = 0
#     if session['count'] += 1