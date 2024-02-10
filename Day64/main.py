from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

MOVIEDB_API = "59a4dbb45f581740aeabe87f469eeaeb"
url = "https://api.themoviedb.org/3/search/movie"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


#CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class RateMovieForm(FlaskForm):
    new_rating = StringField(label="Your Rating Out of 10 e.g.c7.5", validators=[DataRequired()])
    new_review = StringField(label="Your Review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddMovie(FlaskForm):
    title = StringField(label="Movie Title")
    submit = SubmitField(label="Add Movie")


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Float, nullable=False)
    review = db.Column(db.String(250), unique=True, nullable=False)
    img_url = db.Column(db.String(250), unique=True, nullable=False)


with app.app_context():
    db.create_all()

    # new_movie = Movie(
    #     title="Phone Booth",
    #     year=2002,
    #     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    #     rating=7.3,
    #     ranking=10,
    #     review="My favourite character was the caller.",
    #     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    # )
    # all_movies.append(new_movie)
    # db.session.add(new_movie)
    # db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["POST", "GET"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie_to_update = Movie.query.get(movie_id)
    if form.validate_on_submit():
        movie_to_update.rating = float(form.new_rating.data)
        movie_to_update.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie_to_update)


@app.route("/delete", methods=["POST", "GET"])
def delete():
    movie_id = request.args.get('id')
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["POST", "GET"])
def add():
    add_movie = AddMovie()
    if add_movie.validate_on_submit():
        movie_title = add_movie.title.data
        response = requests.get(url, params={"api_key": MOVIEDB_API, "query": movie_title})
        results = response.text[1]
        return render_template("select.html", movies=results)
    return render_template("add.html", form=add_movie)


@app.route("/find")
def find():
    movie_id = request.args.get('id')
    if movie_id:
        response = requests.get(url="https://api.themoviedb.org/3/movie/movie_id",
                                params={"api_key": MOVIEDB_API, "movie_id": movie_id})
        movie = response.json()
        new_movie = Movie(
            title=movie["title"],
            year=movie["release_date"].split("-")[0],
            description=movie["description"],
            img_url=f"{MOVIE_DB_IMAGE_URL}{movie['poster_path']}",
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('edit'))


if __name__ == "__main__":
    app.run(debug=True)
