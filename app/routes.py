from flask import render_template, request, redirect, url_for
from app import app, library

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        library.add_book(title)
        return redirect(url_for('list_books'))
    return render_template('add_book.html')

@app.route('/list_books')
def list_books():
    books = library.list_books()
    return render_template('list_books.html', books=books)

@app.route('/mark_read/<int:index>')
def mark_read(index):
    try:
        library.mark_book_read(index)
    except IndexError:
        pass
    return redirect(url_for('list_books'))

@app.route('/mark_unread/<int:index>')
def mark_unread(index):
    try:
        # This is a workaround to mark a book as unread by setting the `read` attribute to False
        # Alternatively, you could add a method in Library to mark a book as unread
        book = library.list_books()[index]
        book.read = False
    except IndexError:
        pass
    return redirect(url_for('list_books'))
