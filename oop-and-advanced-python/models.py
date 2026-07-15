# ==========================================
# Classes and Inheritance
# ==========================================

class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")


class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def display_info(self):
        super().display_info()
        print(f"Pages: {self.pages}")


class Magazine(LibraryItem):
    def __init__(self, title, author, issue):
        super().__init__(title, author)
        self.issue = issue

    def display_info(self):
        super().display_info()
        print(f"Issue: {self.issue}")