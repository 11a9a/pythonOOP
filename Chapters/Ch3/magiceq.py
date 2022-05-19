# Using the __str__ and __repr__ magic methods


class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: the __eq__ method checks for equality between two objects
    def __eq__(self, book):
        if not isinstance(book, Book):
            raise ValueError("Can't compare a book to a non-book")
        return (self.title == book.title and
                self.author == book.author and
                self.price == book.price)

    # TODO: the __ge__ establishes >= relationship with another obj
    def __ge__(self, book):
        if not isinstance(book, Book):
            raise ValueError("Can't compare a book to a non-book")
        return self.price >= book.price

    # TODO: the __lt__ establishes < relationship with another obj
    def __lt__(self, book):
        if not isinstance(book, Book):
            raise ValueError("Can't compare a book to a non-book")
        return self.price < book.price

    def __str__(self) -> str:
        return self.title


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 39.95)
b4 = Book("To Kill a Mockingbird", "Harper Lee", 24.95)

# TODO: Check for equality
print(b1 == b3)
print(b1 == b2)

# TODO: Check for greater and lesser value
print(b1 >= b2)
print(b1 < b2)

# TODO: Now we can sort them too
books = [b3, b1, b4, b2]
books.sort()
print([str(book) for book in books])
print(b1)