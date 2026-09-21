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
    title = input("Enter the book title to add: ")
    library.append(title)
    print(f'"{title}" has been added to your library.')

def remove_book(library):
    "Remove a book title from the library"
    title = input("Enter the book title to remove:")
    if title in library:
        library.remove(title)
        print(f"{title} has been removed from your library.")
    else:
        print(f"{title} is not in your library.")

def list_books(library):
    "list all books in the library"
    print("All books currently in library:")
    for title in library:
        print(f"- {title}")

def search_book(library):
    "Search for a book in library"
    title = input("Enter the book title to search for :")
    if title in library:
        print(f"{title} by {author} ({year}) is in your library.")
    else:
        print(f"{title} is not in your library.")


    