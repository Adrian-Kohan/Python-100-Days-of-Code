from flask import Flask, render_template
import jinja2

templateLoader = jinja2.FileSystemLoader(
    searchpath="./"
)

app = Flask(__name__)

templateEnv = jinja2.Environment(
  loader=templateLoader,
  comment_start_string='{+',
  comment_end_string='+}',
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cv")
def cv():
    return render_template("cv.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

