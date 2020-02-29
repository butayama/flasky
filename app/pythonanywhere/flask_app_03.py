from flask import Flask, make_response, request

from app.pythonanywhere.processing_03 import process_data

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=["GET", "POST"])
def file_summer_page():
    if request.method == "POST":
        input_file = request.files["input_file"]
        input_data = input_file.stream.read().decode("utf-8")
        output_data = process_data(input_data)
        response = make_response(output_data)
        response.headers["Content-Disposition"] = "attachment; filename=result.csv"
        return response

    return '''
        <html>
            <body>
                <p>Select the file you want to sum up:</p>
                <form method="post" action="." enctype="multipart/form-data">
                    <p><input type="file" name="input_file" /></p>
                    <p><input type="submit" value="Process the file" /></p>
                </form>
            </body>
        </html>
    '''
