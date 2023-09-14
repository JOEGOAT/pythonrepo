from utils import database

USER_CHOICE = """
Enter:\n

- 'a' to add a new book
- 'l' to list all the books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Enter Your Choice: """
def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()

        elif user_input == 'l':
            show_books()

        elif user_input == 'r':
            prompt_mark_book_as_read()

        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown Command,Please Try Again!!")
        user_input = input(USER_CHOICE)

#function to add new book
def prompt_add_book():
    name = input("Enter the name of the new book: ")
    author = input("Name of the Author: ")
    database.add_books(name, author)

#function to list books
def show_books():
    books = database.get_all_books()
    if len(books) >0:
        s = "s" if len(books) == 0 or len(books) != 1 else ""
        print(f"You have {len(books)} books{s} in your collection")
        
        for book in books:
            read = "Yes" if book ['read'] == "1" else "No" # ternary operator/ shorthand if statement
    
    # the longer version of the shorthand if statement
        # read = none
        # if book['read'] == true:
        #     read = "Yes"
        # else:
        # read = "No"

            print(f"{book['name']} written by {book['author']} , Read : {read}")
    
    else :
        print("You have no books at the moment")

# function to mark a book as read 
def prompt_mark_book_as_read():
    name = input("Enter the name of the book you finished reading: ")
    database.mark_book_as_read(name)

#function to delete
def prompt_delete_book():
    name = input(f"Enter the name book to delete: ")
    database.delete_book(name)

#call the menu function
menu()