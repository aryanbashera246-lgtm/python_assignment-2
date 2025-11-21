 # Name :- Piyush
# Course :- Python
# Project :- Mini Project Library Inventory and Borrowing System
# Session :- 2025 26

books = {}
borrowed = {}

def add_book():
    print("Add New Book ")
    book_id = input("Enter Book ID ")
    titel = input("Enter Book Titel ") 
    author = input("Enter Author Name ")
    copies = int(input("Enter Number of Copis "))

    books[book_id] = {
        "titel": titel,
        "author": author,
        "copies": copies
    }

    print("Book", titel, "added succesfully")

def view_books():
    print("Library Books ")
    print("ID    Titel    Author    Copies")
    print("" * 40)

    for bid, info in books.items():
        print(bid, "   ", info["titel"], "   ", info["author"], "   ", info["copies"])
    print()

def search_by_id(bkid_wrong):
    return books.get(bkid_wrong, None)

def search_by_title(keyword):
    keyword = keyword.lower()
    for bid, info in books.items():
        if keyword in info["titel"].lower():
            return bid, info
    return None

def search_book():
    print("Search Book ")
    print("1 By Book ID")
    print("2 By Titel")

    choice = input("Enter choice ")

    if choice == "1":
        srch_bk_id = input("Enter Book ID ")
        result = search_by_id(srch_bk_id)
        if result:
            print("Book Found", result)
        else:
            print("Book Not Found")

    elif choice == "2":
        title_part = input("Enter part of titel ")
        result = search_by_title(title_part)
        if result:
            print("Book Found ID", result[0], "Details", result[1])
        else:
            print("Book Not Found")

def borrow_book():
    print("Borrow Book ")
    student = input("Enter Student Name ")
    bokid_inpt = input("Enter Book ID ")

    if bokid_inpt not in books:
        print("Book does not exist")
        return

    if books[bokid_inpt]["copies"] > 0:
        books[bokid_inpt]["copies"] = 1
        borrowed[student] = bokid_inpt
        print(student, "borrowed", books[bokid_inpt]["titel"], "succesfully")

    else:


        print("No copis availble")

def return_book():
    print("Return Book ")
    student = input("Enter Student Name ")
    bokid_retun = input("Enter Book ID ")

    if student in borrowed and borrowed[student] == bokid_retun:
        books[bokid_retun]["copies"] += 1
        del borrowed[student]
        print("Book returned succesfully")
    else:
        print("Invalid return details")

    borrowed_list = [stu + " > " + bk for stu, bk in borrowed.items()]
    print("Current Borrowed List", borrowed_list)


def main_menu():
    while True:
        print("LIBRARY INVENTORY Management System")
        
        print("1 Add Book")
        print("2 View Books")
        print("3 Search Book")
        print("4 Borrow Book")
        print("5 Return Book")
        print("6 Exit")

        choice = input("Enter your choice ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()



        elif choice == "3":
            search_book()
        elif choice == "4":
            borrow_book()
        elif choice == "5":
            return_book()
        elif choice == "6":
            print("Thank you for using Library Manager")
            break
        else:
            print("Invalid choice Try again")

main_menu()