from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class Dictionary(FlaskForm):
    word = StringField(label="Word")
    search = SubmitField(label="Search")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = Dictionary()
    word = form.word.data
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    if form.validate_on_submit():
        response = requests.get(url)
        data = response.json()
        definitions = []
        examples = []
        if len(data[0]["meanings"][0]["definitions"]) > 3:
            for i in range(0, 3):
                definition = data[0]["meanings"][0]["definitions"][i]["definition"]
                definitions.append(definition)

            for i in range(0, 3):
                if "example" in data[0]["meanings"][0]["definitions"][i]:
                    example = data[0]["meanings"][0]["definitions"][i]["example"]
                    examples.append(example)

        elif len(data[0]["meanings"][0]["definitions"]) < 3:
            for i in range(0, len(data[0]["meanings"][0]["definitions"])):
                definition = data[0]["meanings"][0]["definitions"][i]["definition"]
                definitions.append(definition)

            for i in range(0, len(data[0]["meanings"][0]["definitions"])):
                if "example" in data[0]["meanings"][0]["definitions"][i]:
                    example = data[0]["meanings"][0]["definitions"][i]["example"]
                    examples.append(example)

        return render_template("index.html", form=form, definitions=definitions, word=word, examples=examples)
    return render_template("index.html", form=form, defifintions=[], examples=[])


if __name__ == '__main__':
    app.run(debug=True)
