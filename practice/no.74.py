class book():
    booktype = 'fun'
    def __init__(self, page):
        self.pages = page

my_book = book(540)
asal_book = book(799)
asal_book.booktype = 'horror'

print(f"my book has {my_book.pages}")
print(f"asal's book has {asal_book.pages}")
print(f"my book type is {my_book.booktype}")
print(f"asal's type is {asal_book.booktype}")