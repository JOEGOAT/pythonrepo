#concerned with storing and relieving boooks from a list
books = []

#a function to add a book into the list(database)
def add_books(name,author):
    books.append({
      'name':name,
      'author':author,
      'read':False
    })

#functions to get all the books
def get_all_books():
    return books
    

#function to mark a book as read
def mark_book_as_read(name):
    for book in books:
        if book['name'].lower() == name.lower():
            book['read']=True

#function to delete a book
def delete_book(name):
    for book in books:
        if book['name'].lower()==name.lower():
            #books.remove(book)
            #or
            #books.pop(books.index(book))
            #or
            del book[books.index(book)]
    print(f"P{book['name']} deleted Successfully!!")