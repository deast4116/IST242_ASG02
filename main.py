

def display_menu():
    "Display the first menu that appears when the program is run"
    print("\n === Personal Library Manager===")
    print("1. Add a book title")
    print("2. Remove a book title")
    print("3. List all book titles")
    print("4. Search for a book title")
    print("5. Exit")


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
