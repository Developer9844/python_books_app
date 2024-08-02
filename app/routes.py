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
        book = library.list_books()[index]
        book.read = False
    except IndexError:
        pass
    return redirect(url_for('list_books'))

@app.route('/edit_book/<int:index>', methods=['GET', 'POST'])
def edit_book(index):
    try:
        book = library.list_books()[index]
        if request.method == 'POST':
            new_title = request.form['title']
            book.title = new_title
            return redirect(url_for('list_books'))
        return render_template('edit_book.html', book=book, index=index)
    except IndexError:
        return redirect(url_for('list_books'))

@app.route('/delete_book/<int:index>')
def delete_book(index):
    try:
        del library.list_books()[index]
    except IndexError:
        pass
    return redirect(url_for('list_books'))
