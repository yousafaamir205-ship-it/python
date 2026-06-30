from book import Book
class Library:
    def __init__(self):
        self.book=[]
    def add_book(self):
        id=int(input("enter id"))
        title=str(input("enter title"))
        author=str(input("enter author"))

        b1=Book(title,author,id)
        self.book.append(b1)
        print("book added successfully")
    def view_book(self):
        if not self.book:
            print("no book available")
        else:
    
            for book in self.book:
                book.displayBooks()
    def search_book(self):
        i=int(input("enter book id"))
        for n in self.book:
            if(i==n.BookID):
                n.displayBooks()
                break
        else:
            print("book not found")

    def borrow_book(self):
        i=int(input("enter id"))
        for n in self.book:
            if i==n.BookID:
                n.borrowBook()
                print("book found")
                break
        else:
                print ("book not found")
    def return_book(self):
        i=int(input("input id"))
        for n in self.book:
            if i==n.BookID:
                n.returnB()
                break
        else:
                print("book not found")
    def remove_book(self):
        i=int(input("enter id"))
        for n in self.book:
            if i==n.BookID:
                self.book.remove(n)
        else:
            print("book not found")

