from flask import Flask, render_template

app = Flask("__name__")


@app.route("/")
def home():
    return render_template("home.html")


# @app.route("/api/v1/<definition>/<word>")
@app.route("/api/v1/<word>")
def api(word):
    definition = word.upper()
    result_dict = {"definition": definition,"word": word}
    return result_dict


if __name__ == "__main__":
    app.run(debug=True, port=5501)