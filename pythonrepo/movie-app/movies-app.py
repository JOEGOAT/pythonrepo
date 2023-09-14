#Create a menu frm the user to choose frm
MENU_PROMPT="\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

#create an empty list to store the movies
movies=[]


#create a function to display the menu
def add_movie():
    title = input("Enter the Movie Title: ")
    director = input("Enter the Movie Director: ")
    year = input("Enter the Movie Release year: ")

    #Append the movies as a dictionary to the movies list
    movies.append({
        'title': title,
        'director':director,
        'year':year
    })

#A function to list all movies
def list_movies():
    #hint -> use a for loop
    for movie in movies:
        print_movie(movie)

# A function to find a movie by its title
def find_movie():
    title_name = input("Enter Movie Title: ")
    for movie in movies:
        if movie['title'] == title_name:
            print(f"{movie['title']} directed by {movie['director']} release year is {movie['year']}")

#Create a helper function to display the movie in a nice formart
def print_movie(movie):
    #print(f"Movie Title: {movie['title']}")
    #print(f"Movie Director: {movie['director']}")
    #print(f"Release Year: {movie['Year']}")
    print(f"{movie['title']} directed by {movie['director']},was released in {movie['year']}")
#Get the user choice
def menu():
    selection = input(MENU_PROMPT)
    while selection !='q':
        #"!=" means not equals to
        if selection =='a':
            add_movie()
        elif selection =='l':
            list_movies()
        elif selection =='f':
            find_movie()
        else:
            print("Unknown Command,Please Try Again.")
        selection = input(MENU_PROMPT)

menu()