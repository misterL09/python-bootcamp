class Book:
    def __init__(self, title=None, genre=None, author=None):
        self.title = title
        self.genre = genre
        self.author = author

    def __repr__(self):
        return f"{self.title}[{self.genre}] - {self.author}"

book1 = Book("The Hobbit", "Fantasy", "Tolkien")
book2 = Book("Dune", "Sci - Fi", "Herbert")
print(book1)


