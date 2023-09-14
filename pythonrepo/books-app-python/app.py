from utils import database

USER_CHOICE = """
Enter:

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

#create a function to prompt the user to add a new book
def prompt_add_book():
    name = input("Enter the name of the new book: ")
    author = input("Name of the Author: ")
    database.add_books(name, author)

#Create a function to show all books
def show_books():
    all_books = database.get_all_books()
    if len(all_books) > 0:
          s="s" if(len(all_books)) ==0 or len(all_books) !=1 else ""
          print(f"You have {len(all_books)} book{s} in your collection")
          for book in all_books:
        #short handed method/ternary operator
            read="Yes" if book ['read'] is True else "No"

        #or
        #long handed method
        #for book in all_books:
            #read=None
        #if book['read']==True:
            #read="Yes"
        #else:
            #read="No"

            print(f"{book['name']} written by {book['author']}, Read: {read}")
    else:
        print("You have no books at the moment.")
#   Or

    

#Create a function to prompt the user to mark a book as read
def prompt_mark_book_as_read():
    name=input("Enter the name of the book you have finished reading: ")
    database.mark_book_as_read(name)

#Create a function to delete a book
def prompt_delete_book():
    name=input("Enter the name of the book you wish to delete: ")
    database.delete_book(name)

#call the menu function
menu()