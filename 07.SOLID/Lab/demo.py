class Printer:
    def print(self, message):
        print(message)


class FilePrinter(Printer):
    def print(self, message, file_name):
        print(f'{file_name} - {message}')
