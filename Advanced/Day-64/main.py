from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from movie import db, Movie
from movie_form import MovieForm
from rate_movie_form import RateMovieForm
import requests

MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_API_KEY = 'b2eac59d6c813cfa75903c5dea7b9473'   # your API key here
MOVIE_DB_INFO_URL = 'https://api.themoviedb.org/3/movie'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie-collection.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)


@app.route('/add', methods=['GET', 'POST'])
def add():
    movie_form = MovieForm()
    if movie_form.validate_on_submit():
        movie_title = movie_form.title.data
        response = requests.get(
            MOVIE_DB_SEARCH_URL,
            params={
                "api_key": MOVIE_DB_API_KEY,
                "query": movie_title
            }
        )
        data = response.json()['results']
        return render_template("select.html", options=data)
    return render_template('add.html', form=movie_form)


@app.route("/update", methods=['GET', "POST"])
def update():
    rate_form = RateMovieForm()
    if rate_form.validate_on_submit():
        movie_to_update = Movie.query.get(request.args.get('id'))
        movie_to_update.rating = rate_form.rating.data
        movie_to_update.review = rate_form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    movie_id = request.args.get('id')
    movie_selected = Movie.query.get(movie_id)
    return render_template("edit.html", form=rate_form, movie=movie_selected)


@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    with app.app_context():
        movie_to_delete = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/find')
def find_movie():
    movie_api_id = request.args.get('id')
    if movie_api_id:
        movie_api_url = f'{MOVIE_DB_INFO_URL}/{movie_api_id}'
        response = requests.get(
            movie_api_url,
            params={
                "api_key": MOVIE_DB_API_KEY,
                "language": "en-US"
            }
        )
        data = response.json()
        new_movie = Movie(
            title=data['title'], year=data['release_date'].split('-')[0],
            image_url=f"{movie_api_url}{data['poster_path']}?api_key={MOVIE_DB_API_KEY}",
            description=data['overview']
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
