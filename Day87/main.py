from flask import Flask, render_template, redirect, url_for,  jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL


app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    map_url = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    image = StringField('Cafe image (URL)', validators=[DataRequired(), URL()])
    location = StringField('Cafe location', validators=[DataRequired()])
    seats = StringField('Number of seats', validators=[DataRequired()])
    has_toilet = SelectField('Does Cafe has toilet?', choices=["True", "False"], validators=[DataRequired()])
    has_wifi = SelectField('Does Cafe has wifi?', choices=["True", "False"], validators=[DataRequired()])
    has_sockets = SelectField('Does Cafe has sockets?', choices=["True", "False"], validators=[DataRequired()])
    can_take_calls = SelectField('Can we take calls at there?', choices=["True", "False"], validators=[DataRequired()])
    coffee_price = StringField('What is the price of coffee?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class SearchForm(FlaskForm):
    search = StringField(validators=[DataRequired()])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/cafes', methods=['POST', 'GET'])
def cafes():
    search_form = SearchForm()
    searched_cafe = search_form.search.data
    cafe = db.session.query(Cafe).filter_by(name=searched_cafe).first()
    if search_form.validate_on_submit():
        if cafe:
            return render_template('search.html', cafe=cafe)
        else:
            return render_template('status.html', message="Sorry, we couldn't find the cafe.",
                                   heading="Not Found", status=404)
    all_cafes = Cafe.query.all()
    list_of_cafes = [cafe.to_dict() for cafe in all_cafes]
    return render_template('cafes.html', cafes=list_of_cafes, search=search_form)


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = Cafe(
            name=form.cafe.data,
            map_url=form.map_url.data,
            img_url=form.image.data,
            location=form.location.data,
            has_sockets=bool(form.has_sockets.data),
            has_toilet=bool(form.has_toilet.data),
            has_wifi=bool(form.has_wifi.data),
            can_take_calls=bool(form.can_take_calls.data),
            seats=form.seats.data,
            coffee_price=form.coffee_price.data,
        )
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for("cafes"))
    return render_template('add.html', form=form, h1="Add a new cafe into the database")


# ["PATCH"]


@app.route("/update-cafe/<cafe_id>", methods=["POST", "GET"])
def edit_cafe(cafe_id):
    cafe = db.session.query(Cafe).get(cafe_id)
    edit_form = CafeForm(
        cafe=cafe.name,
        map_url=cafe.map_url,
        image=cafe.img_url,
        location=cafe.location,
        seats=cafe.seats,
        has_toilet=cafe.has_toilet,
        has_wifi=cafe.has_wifi,
        has_sockets=cafe.has_sockets,
        can_take_calls=cafe.can_take_calls,
        coffee_price=cafe.coffee_price,
    )
    if edit_form.validate_on_submit():
        cafe.name = edit_form.cafe.data
        cafe.map_url = edit_form.map_url.data
        cafe.img_url = edit_form.image.data
        cafe.location = edit_form.location.data
        cafe.seats = edit_form.seats.data
        cafe.has_toilet = bool(edit_form.has_toilet.data)
        cafe.has_wifi = bool(edit_form.has_wifi.data)
        cafe.has_sockets = bool(edit_form.has_sockets.data)
        cafe.can_take_calls = bool(edit_form.can_take_calls.data)
        cafe.coffee_price = edit_form.coffee_price.data
        db.session.commit()
        return redirect(url_for("cafes", cafe_id=cafe.id))
    return render_template("add.html", form=edit_form, is_edit=True, h1="Edit Cafe")


# methods=["DELETE"]


@app.route("/report-closed/<cafe_id>")
def delete_the_cafe(cafe_id):
    api_key = request.args.get("api_key")
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        if api_key == "TopSecretAPIKey":
            db.session.delete(cafe)
            deb.session.commit()
            return render_template('status.html', message="Successfully deleted the cafe from the database.",
                                   heading="success", status=200)
        else:
            return render_template('status.html', message="Sorry, that's not allowed. "
                                                          "Make sure you have the correct api_key.",
                                   heading="Forbidden", status=403)
    else:
        return render_template('status.html', message="Sorry a cafe with that id was not found in the database.",
                               heading="Not Found", status=404)


if __name__ == '__main__':
    app.run(debug=True)
