#concerned with storing and relieving boooks from a list


#a function to add a book into the list(database)
def add_books(name,author):
    with open(file, "a") as f:
        f.write(f"{name},{author},0\n") 

#functions to get all the books
def get_all_books():
    pass

#function to mark a book as read
def mark_book_as_read(name):
    pass
#function that save all books in the file
def _save_all_books(books):
    pass

#function to delete a book
def delete_book(name):
    pass
