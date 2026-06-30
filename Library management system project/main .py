from library import Library
while True:
    print("======library management system======")
    print("1. Add book")
    print("2. view book")
    print("3. search book")
    print("4. borrow book")
    print("5. return book")
    print("6. remove book")
    print("7. exit")

    choice=int(input("enter your choice:"))
    if choice==1:
        Library.add_book()
    elif choice==2:
        Library.view_book()
    elif choice==3:
        Library.search_book()
    elif choice==4:
        Library.borrow_book()
    elif choice==5:
        Library.return_book()
    elif choice==6:
        Library.remove_book()
    elif choice==7:
        print("program has been exited")