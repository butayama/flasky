from flask import Flask, request, session

from app.pythonanywhere.processing_02 import calculate_mode

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "lkmaslkdsldsamdlsdmasldsmkdd"


@app.route("/", methods=["GET", "POST"])
def mode_page():
    if "inputs" not in session:
        session["inputs"] = []

    errors = ""
    if request.method == "POST":
        try:
            session["inputs"].append(float(request.form["number"]))
            session.modified = True
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number"])

        if request.form["action"] == "Calculate number":
            result = calculate_mode(session["inputs"])
            session["inputs"].clear()
            session.modified = True
            return '''
                <html>
                    <body>
                        <p>{result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)

    if len(session["inputs"]) == 0:
        numbers_so_far = ""
    else:
        numbers_so_far = "<p>Numbers so far:</p>"
        for number in session["inputs"]:
            numbers_so_far += "<p>{}</p>".format(number)

    return '''
        <html>
            <body>
                {numbers_so_far}
                {errors}
                <p>Enter your number:</p>
                <form method="post" action=".">
                    <p><input name="number" /></p>
                    <p><input type="submit" name="action" value="Add another" /></p>
                    <p><input type="submit" name="action" value="Calculate number" /></p>
                </form>
            </body>
        </html>
    '''.format(numbers_so_far=numbers_so_far, errors=errors)
