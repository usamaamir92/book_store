from lib.book import *

class BookRepository():
    def __init__(self,connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM books')
        books = []
        for row in rows:
            item = Book(row["title"],row["author_name"])
            books.append(item)
        return books