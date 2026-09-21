import json




def display_menu():
    "Display the first menu that appears when the program is run"
    print("\n === Personal Library Manager===")
    print("1. Add or update a book title")
    print("2. Remove a book title")
    print("3. List all book titles")
    print("4. Search for a book ")
    print("5. Show Author stats")
    print("6. Save and exit")

def load_library(filename):
    "load library from json file"
    try:
        with open(filename, 'r') as file:
            library = json.load(file)

            if isinstance(library, dict):
                return library
            else:
                return {}
    except FileNotFoundError:
        return {}

def save_library(library, filename):
    "save library to json file"
    with open(filename, 'w') as file:
        json.dump(library, file, indent=4)

    
def add_book(library):
    "Add a book title to the library"
    title = input("Enter the book title to add: ").strip()
    author = input("Enter the author of the book: ").strip()

    while True:
        try:
            year = int(input("Enter the year of publication: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a valid year(whole number).")

    if title in library:
        result = "updated"
    else:
        result = "added"

    library[title] = {"author": author, "year": year}
    print(f"{title} has been {result} in your library.")

def remove_book(library):
    "Remove a book title from the library"
    title = input("Enter the book title to remove:").strip()
    

    if title in library:
        del library[title]
        print(f"{title} has been removed from your library.")
    else:
        print(f"{title} is not in your library.")

def list_books(library):
    "list all books in the library"

    number = 1

    for title in books:
        author = library[title]["author"]
        year = library[title]["year"]
        print(f"{number}. {title} by {author} ({year})")
        number += 1


def search_book(library):
    "Search for a book in library"
    title = input("Enter the book title to search for :")
    if title in library:
        print(f"{title} by {author} ({year}) is in your library.")
    else:
        print(f"{title} is not in your library.")


    