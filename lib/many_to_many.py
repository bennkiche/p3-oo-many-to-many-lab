class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        """Return all contracts associated with this book."""
        return [contract for contract in Contract.all_contracts if contract.book == self]

    def authors(self):
        """Return all unique authors associated with this book."""
        return list({contract.author for contract in self.contracts()})


class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all_authors.append(self)

    def contracts(self):
        """Return all contracts associated with this author."""
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        """Return all unique books associated with this author."""
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        """Sign a new contract for a book with specified details."""
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Calculate the total royalties earned by this author."""
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        """Return contracts for a specific date, sorted by author name and book title."""
        if not isinstance(date, str):
            raise Exception("date must be a string")
        contracts_on_date = [contract for contract in cls.all_contracts if contract.date == date]
        # Sort by author name, book title, and ID to ensure deterministic order
        return sorted(contracts_on_date, key=lambda c: (c.author.name, c.book.title, id(c)))
