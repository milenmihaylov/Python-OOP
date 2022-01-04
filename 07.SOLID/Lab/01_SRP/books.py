class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f'Title: {self.title}, Author: {self.author}'


class Library:
    def __init__(self):
        self.__books = []

    def add_book(self, value: Book):
        if isinstance(value, Book):
            self.__books.append(value)

    def find_book(self, title):
        return '\n'.join([str(b) for b in self.__books if title in b.title])

    def __str__(self):
        return 'Books:\n' + '\n'.join([f'Title: {x.title}, Author: {x.author}' for x in self.__books])


harry_potter = Book('Harry Potter', 'J. K. Rowling')
b_library = Library()
b_library.add_book(harry_potter)
song_for_ice_and_fire = Book('Winter is coming', 'George RR Martin')
b_library.add_book(song_for_ice_and_fire)

print(b_library.find_book('Wintefdgr'))

