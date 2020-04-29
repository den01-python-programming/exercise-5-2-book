import pytest
from src.book import Book

def test_exercise():
    book = Book("J.R.R. Tolkein", "Lord of the Rings", "1000")

    assert book.get_name() == "J.R.R. Tolkein"
    assert book.get_pages() == "Lord of the Rings"
    assert book.get_author() == "1000"
    assert str(book) == "J.R.R. Tolkein, Lord of the Rings, 1000 pages"
