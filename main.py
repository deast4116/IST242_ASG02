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
    title = input("Enter the book title to search for :").strip().lower()
    match = {}

    for title in library:
        if title.lower() == title:
            match[title] = library[title]

    if len(match) == 0:
        print(f"{title} is not in your library.")
    else:
        list_books(match)

def show_author_stats(library):
    "Show number of books written by each author in the library"
    stats = {}

    for title in library:
        author = library[title]["author"]

        if author in stats:
            stats[author] += 1
        else:
            stats[author] = 1

    if len(stats) == 0:
        print("No books in your library.")
    else:
        print("Books per author:")
        for author in stats:
            print(f"{author}: {stats[author]} book(s)")
    
def main():
    "Run main program"
    filename = "library.json"
    library = load_library(filename)

    print(f"Loaded {len(library)} books from {filename}.")

    while True:
        display_menu()
        choice = input("Enter your choice (1-6):").strip()

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            list_books(library)
        elif choice == "4":
            search_book(library)
        elif choice == "5":
            show_author_stats(library)
        elif choice == "6":
            save_library(library, filename)
            print(f"Library saved to {filename}. See you next time.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if name__ == "__main__":
    main()

    