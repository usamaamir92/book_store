from lib.book_repository import *

def test_get_all_books(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    books = repository.all()
    assert books == [
        Book('Nineteen Eighty-Four', 'George Orwell'),
        Book('Mrs Dalloway', 'Virginia Woolf'),
        Book('Emma', 'Jane Austen'),
        Book('Dracula', 'Bram Stoker'),
        Book('The Age of Innocence', 'Edith Wharton')
        ]