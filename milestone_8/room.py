from faker import Faker
from faker.providers import DynamicProvider

fake = Faker()
books_pile = []
books_count = 10

Faker.seed(0)

genres_provider = DynamicProvider(
     provider_name="genres",
     elements=["detective", "adventure", "scifi", "horror", "triller", "classic"],
)
fake.add_provider(genres_provider)


class Bookcase:

    def __init__(self):
        self.shelves = dict()

    def add_book(self, book, shelf=None):
        if shelf is None:
            if book.genre not in self.shelves:
                self.shelves[book.genre] = Shelf()
            return self.shelves[book.genre].add_book(book)
        else:
            shelf2 = self.get_shelf(book.genre)
            if shelf2 is None or shelf2 == shelf:
                return shelf.add_book(book)
            else:
                return False

    def show_shelves(self):
        visited_shelves = set()
        for genre in self.shelves:
            if self.shelves[genre] in visited_shelves:
                continue
            visited_shelves.add(self.shelves[genre])
            self.shelves[genre].show_books()

    def remove_book(self, book):
        shelf = self.get_shelf(book.genre)
        if shelf is not None:
            return shelf.remove_book(book)
        else:
            return False

    def get_shelf(self, genre):
        return None if genre not in self.shelves else self.shelves[genre]


class Shelf:

    def __init__(self):
        self.books = dict()

    def add_book(self, book):
        if book.genre not in self.books:
            self.books[book.genre] = dict()
        self.books[book.genre][book.title] = book
        return True

    def remove_book(self, book):
        if book.genre not in self.books:
            return False
        elif book.titel not in self.books[book.genre]:
            return False
        else:
            del self.books[book.genre][book.titel]
            return True

    def show_books(self):
        print("show_books")
        for genre in self.books:
            print(f'\tgenre : {genre}')
            for title in self.books[genre]:
                print(f"\t\t{self.books[genre][title]}")
            print("\n")


class Book:
    def __init__(self, author, title, genre):
        self.author = author
        self.title = title
        self.genre = genre

    def __str__(self):
        return f'author: {self.author} title: "{self.title}" genre: {self.genre}'


for _ in range(books_count):
    books_pile.append(Book(fake.unique.name(), fake.texts(nb_texts=1, max_nb_chars=25)[0], fake.genres()))

bc1 = Bookcase()
# print(books_pile)
for book in books_pile:
    # print(book)
    bc1.add_book(book)

bc1.show_shelves()

bc2 = Bookcase()
book1 = Book("Agata Cristi", "12 niggers", "detective")
book2 = Book("NIll Gameman", "American Gods", "adventure")
book3 = Book("Conan Doyle", "Sherlok Holmes", "detective")
book4 = Book("Stiven King", "1408", "horror")

bc2.add_book(book2)

bc2.add_book(book1, bc2.get_shelf('adventure'))
bc2.show_shelves()
bc2.add_book(book4)
bc2.show_shelves()
bc2.add_book(book3, bc2.get_shelf('horror'))