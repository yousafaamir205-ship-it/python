class Book:
    def __init__(self,title,author,BookID):
        self.availability=True
        self.title=title
        self.author=author
        self.BookID=BookID
    def displayBooks(self):
        print("BOOK ID: ",self.BookID)
        print("book title",self.title)
        print("book author: ",self.author)
        if self.availability:
            print("available")
        else:
            print("not available")
    def borrowBook(self):
        if self.availability :
            print("book is available: ")
            self.availability=False
        else:
            print("book is not available")
    def returnB(self):
        if self.availability==False:
            self.availability=True
            print("book returned successfully")
        else:
            print("book is already available")

    
book1=Book(101,"pyhton","jerry")