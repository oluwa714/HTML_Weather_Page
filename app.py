from flask import Flask, render_template
import jinja2
import pandas as pd
import os

path = os.path.join("Resources", "cities.csv")

app = Flask(__name__, static_url_path="/static")


@app.route("/")
def landing_page():
    return render_template("landing_page.html")


@app.route("/vis_page_1")
def visualization_one():
    return render_template("vis_page_1.html")


@app.route("/vis_page_2", methods=["GET", "POST"])
def visualization_two():
    return render_template("vis_page_2.html")


@app.route("/vis_page_3")
def visualization_three():
    return render_template("vis_page_3.html")


@app.route("/vis_page_4")
def visualization_four():
    return render_template("vis_page_4.html")


@app.route("/comparison")
def compare_all():
    return render_template("comparison.html")


@app.route("/data_table")
def data_table():
    df = pd.read_csv(path)
    return render_template(
        "data_table.html", title="Data Table", data=list(df.values.flatten())
    )


if __name__ == "__main__":
    app.run(debug=True)
