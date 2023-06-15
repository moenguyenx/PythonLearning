from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from book_form import BookForm
from rating_form import RatingForm
from book_db import Book, db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dudewtf'
Bootstrap(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///book-collection.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(title=form.title.data, author=form.author.data, rating=form.rating.data)
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html', form=form)


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    rating_form = RatingForm()
    if rating_form.validate_on_submit():
        book_to_update = Book.query.get(request.args.get('id'))
        book_to_update.rating = rating_form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    return render_template('edit_rating.html', book=book_selected, form=rating_form)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
