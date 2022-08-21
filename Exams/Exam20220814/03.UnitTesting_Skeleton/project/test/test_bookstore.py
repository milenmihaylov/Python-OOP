import unittest

from project.bookstore import Bookstore
# from bookstore import Bookstore


class TestBookstore(unittest.TestCase):

    def test_init__total_sold_books__len(self):
        limit = 1
        store = Bookstore(limit)
        self.assertEqual(limit, store.books_limit)
        self.assertEqual({}, store.availability_in_store_by_book_titles)
        self.assertEqual(0, store.total_sold_books)
        self.assertEqual(0, len(store))

    def test_books_limit_bad_value(self):
        limit = 0
        expected_msg = f"Books limit of {limit} is not valid"
        with self.assertRaises(ValueError) as context:
            Bookstore(limit)
        self.assertEqual(expected_msg, str(context.exception))

    def test_receive_book_valid(self):
        limit = 10
        store = Bookstore(limit)
        title = 'HarryPotter'
        copies = 10
        actual_msg = store.receive_book(title, copies)
        expected = f"{copies} copies of {title} are available in the bookstore."
        self.assertEqual(expected, actual_msg)

    def test_receive_book_bad_limit(self):
        limit = 9
        store = Bookstore(limit)
        title = 'HarryPotter'
        copies = 10
        expected = "Books limit is reached. Cannot receive more books!"
        with self.assertRaises(Exception) as context:
            store.receive_book(title, copies)
        self.assertEqual(expected, str(context.exception))

    def test_receive_book__test_title(self):
        limit = 20
        store = Bookstore(limit)
        title = 'HarryPotter'
        copies = 10
        store.receive_book(title, copies)
        actual_msg = store.receive_book(title, copies)
        expected = f"{copies * 2} copies of {title} are available in the bookstore."
        self.assertEqual(expected, actual_msg)

    def test_len(self):
        limit = 20
        store = Bookstore(limit)
        title = 'HarryPotter'
        copies = 10
        store.receive_book(title, copies)
        store.receive_book('Book2', 10)
        self.assertEqual(20, len(store))

    def test_sell_book__bad_title(self):
        limit = 10
        store = Bookstore(limit)
        title = 'HarryPotter'
        with self.assertRaises(Exception) as context:
            store.sell_book(title, 1)
        self.assertEqual(f"Book {title} doesn't exist!", str(context.exception))

    def test_sell_book__bad_number(self):
        limit = 10
        store = Bookstore(limit)
        title = 'HarryPotter'
        copies = 1
        store.receive_book(title, copies)
        with self.assertRaises(Exception) as context:
            store.sell_book(title, 2)
        self.assertEqual(f"{title} has not enough copies to sell. Left: {copies}", str(context.exception))

    def test_sell_book_valid(self):
        limit = 10
        store = Bookstore(limit)
        title = 'HarryPotter'
        copies = 5
        store.receive_book(title, copies)
        actual_msg = store.sell_book(title, 4)
        self.assertEqual(f"Sold {4} copies of {title}", actual_msg)
        self.assertEqual(4, store.total_sold_books)
        self.assertEqual(1, store.availability_in_store_by_book_titles[title])

    def test_str(self):
        limit = 10
        store = Bookstore(limit)
        title = 'HarryPotter'
        copies = 5
        store.receive_book(title, copies)
        store.sell_book(title, 4)
        msg = f"Total sold books: {store.total_sold_books}\n" \
              f"Current availability: {len(store)}\n" \
              f" - {title}: {1} copies"
        self.assertEqual(msg, str(store))


if __name__ == '__main__':
    unittest.main()
