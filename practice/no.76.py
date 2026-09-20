class book():
    def __init__(self, name, page):
        self.name = name
        self.page = page

    def open(self):
        return(f"i opened {self.name} book which has {self.page} pages.")

    def __len__(self):
        return self.page


class school(book):
    def __init__(self, name, page, grade, subject):
        super().__init__(name, page)
        self.grade = grade
        self.subject = subject

    def open(self):
        return(f"i opened {self.name} book which has {self.page} pages and it's {self.subject} from {self.grade} grade.")
    
saman_book = book('good girls guide to murder', 350)
m = saman_book.open()

yasna_book = school('matrix', 700, 12, 'math')
n = yasna_book.open()

print(m)
print(n)
print(len(saman_book))