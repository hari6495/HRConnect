from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from task_one import do_task_one
from task_two import do_task_two


app = Flask(__name__)
# breakpoint()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        url = url_for(task)
        return redirect(url)
    else:
        return "<h1>Home page...</h1>"


@app.route("/api/taskone")
def taskone():
    # json.dumps(do_task_one())
    # render_template("taskone.html", taskone = json.dumps(do_task_one()))
    return json.dumps(do_task_one())


@app.route("/api/tasktwo")
def tasktwo():
    return jsonify(do_task_two())


if __name__ == "__main__":
    app.run(debug=True)