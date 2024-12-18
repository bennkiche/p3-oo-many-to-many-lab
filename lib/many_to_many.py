class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return list(set(contract.book for contract in self.contracts()))

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list(set(contract.author for contract in self.contracts()))


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self._validate_author(author)
        self._validate_book(book)
        self._validate_date(date)
        self._validate_royalties(royalties)

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]

    @staticmethod
    def _validate_author(author):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")

    @staticmethod
    def _validate_book(book):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")

    @staticmethod
    def _validate_date(date):
        if not isinstance(date, str):
            raise Exception("Date must be a string")

    @staticmethod
    def _validate_royalties(royalties):
        if not isinstance(royalties, int):
            raise Exception("Royalties must be an integer")