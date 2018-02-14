from flask import Flask, render_template, redirect, request, session, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = "trustno1"

TASKS = []

@app.route("/")
def index():
	if "started" not in session:
		session["started"] = "False"
	return render_template("index.html", time=datetime.now(), tasks = TASKS)

@app.route("/start", methods=["POST"])
def start():
	task = {
		"task": request.form["task"],
		"start": datetime.now(),
		"end": None
	}
	TASKS.append(task)
	session["started"] = "True"
	return redirect("/")

@app.route("/stop")
def stop():
	TASKS[-1]["end"] = datetime.now()
	session["started"] = "False"
	return redirect("/")

@app.route("/clear")
def clear():
	session.clear()
	TASKS = []
	return redirect("/")

app.run(debug=True)