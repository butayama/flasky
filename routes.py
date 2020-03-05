from flasky import app
from flask import render_template


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)


@app.route("/case")
def case():
    return render_template("home/case.html", case=True)


@app.route("/op_planning")
def op_planning():
    return render_template("home/op_planning.html", op_planning=True)


@app.route("/op")
def op():
    return render_template("home/op.html", op=True)


@app.route("/post_op")
def post_op():
    return render_template("home/post_op.html", post_op=True)

