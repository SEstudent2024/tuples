# 2. Python Data Structure Challenges in Real-World Scenarios
# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

# Existing Library Data:

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Add functionality to insert new books into `library`. 
# Ensure that adding a duplicate book is handled appropriately.

def add_book(library, title, author):
    """
    Adds a new book to the library if it doesn't already exist.

    Args:
        library (list): The current list of books in the library.
        title (str): The title of the new book.
        author (str): The author of the new book.

    Returns:
        list: The updated list of books in the library.
    """
    new_book = (title, author)
    
    if new_book in library:
        print(f"The book '{title}' by {author} already exists in the library.")
    else:
        library.append(new_book)
        print(f"The book '{title}' by {author} has been added to the library.")
    
    return library

library = add_book(library, "To Kill a Mockingbird", "Harper Lee")
library = add_book(library, "1984", "George Orwell")  # This is a duplicate

print("Updated Library Data:")
for book in library:
    print(book)