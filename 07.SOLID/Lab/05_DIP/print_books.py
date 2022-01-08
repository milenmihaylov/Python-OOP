class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    # def __init__(self, book: Book):
    #     self.book = book
    @staticmethod
    def format(book: Book) -> str:
        return book.content


class UpperCaseFormatter(Formatter):
    @staticmethod
    def format(book: Book) -> str:
        return book.content.upper()


class Printer:
    def __init__(self, formatter: Formatter):
        self.formatter = formatter

    def get_book(self, book: Book):
        formatted_book = self.formatter.format(book)
        return formatted_book


b = Book("Hello beautiful world")
reg_format = Formatter()
upp_format = UpperCaseFormatter()

reg_printer = Printer(reg_format)
upp_printer = Printer(upp_format)

print(reg_printer.get_book(b))
print(upp_printer.get_book(b))
