from lib.book import *

def test_book_constructs():
    book = Book("Test Title","Test Author")
    assert book.title == "Test Title"
    assert book.author_name == "Test Author"