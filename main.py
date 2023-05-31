from flask import Flask, render_template
import pandas as pd

app = Flask("__name__")


@app.route("/")
def home():
    return render_template("home.html")


# @app.route("/api/v1/<definition>/<word>")
@app.route("/api/v1/<word>/")
def api(word):
    df = pd.read_csv("dictionary.csv")
    definition = df.loc[df["word"] == word]['definition'].item()
    result_dict = {"word": word, "definition": definition}
    return result_dict


if __name__ == "__main__":
    app.run(debug=True, port=5502)
