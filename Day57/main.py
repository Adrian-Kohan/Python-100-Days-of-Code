from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/a36c193adde76ca4a7dc")
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route('/blog/<int:num>')
def blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()
    return render_template("post.html", posts=posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)

