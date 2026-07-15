from decorators import logger
from generators import book_titles
from iterators import Countdown
from models import Book, Magazine


@logger
def display_library():

    book1 = Book("Python Crash Course", "Eric Matthes", 544)
    book2 = Book("Automate the Boring Stuff", "Al Sweigart", 592)
    magazine = Magazine("AI Monthly", "OpenAI", "July 2026")

    items = [book1, book2, magazine]

    print("\n===== Library Items =====\n")

    for item in items:
        item.display_info()
        print()


@logger
def generator_demo():

    books = [
        Book("Python Crash Course", "Eric Matthes", 544),
        Book("Deep Learning", "Ian Goodfellow", 775),
        Book("Hands-On ML", "Aurélien Géron", 850)
    ]

    print("\nBook Titles:")

    for title in book_titles(books):
        print(title)


@logger
def iterator_demo():

    print("\nCountdown:")

    for number in Countdown(5):
        print(number)


if __name__ == "__main__":

    display_library()

    generator_demo()

    iterator_demo()