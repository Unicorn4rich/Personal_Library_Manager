import streamlit as st #type: ignore

# Load the library from a file (if it exists)
def load_library():
    try:
        with open("library.txt", "r") as file:
            return eval(file.read())
    except FileNotFoundError:
        return []

# Save the library to a file
def save_library(books):
    with open("library.txt", "w") as file:
        file.write(str(books))

# Main function for the app
def personal_library_manager():
    st.title("Personal Library Manager")
    
    # Load library data
    books_library = load_library()

    # Display the books in the library
    if len(books_library) == 0:
        st.write("Your library is empty!")
    else:
        st.write("### Your Library")
        for idx, book in enumerate(books_library, 1):
            st.write(f"{idx}. {book['title']} by {book['author']} (Genre: {book['genre']}, Published: {book['publication']}) - Read: {book['read']}")

    # Sidebar for navigation
    st.sidebar.title("Options")
    option = st.sidebar.radio("Choose an option", ["Add a Book", "Remove a Book", "Search for a Book", "Display Statistics", "Save & Exit"])

    # Add a Book
    if option == "Add a Book":
        st.subheader("Add a Book")
        title = st.text_input("Enter the book title:")
        author = st.text_input("Enter the author:")
        publication = st.text_input("Enter the publication year:")
        genre = st.text_input("Enter the genre:")
        read = st.selectbox("Have you read this book?", ["Yes", "No"])

        if st.button("Add Book"):
            new_book = {
                "title": title,
                "author": author,
                "publication": publication,
                "genre": genre,
                "read": read
            }
            books_library.append(new_book)
            save_library(books_library)
            st.success("Book added successfully!")

    # Remove a Book
    elif option == "Remove a Book":
        st.subheader("Remove a Book")
        book_titles = [book['title'] for book in books_library]
        book_to_remove = st.selectbox("Select a book to remove:", book_titles)

        if st.button("Remove Book"):
            books_library = [book for book in books_library if book['title'] != book_to_remove]
            save_library(books_library)
            st.success(f"Book '{book_to_remove}' removed successfully!")

    # Search for a Book
    elif option == "Search for a Book":
        st.subheader("Search for a Book")
        search_method = st.radio("Search by:", ["Title", "Author"])

        if search_method == "Title":
            search_title = st.text_input("Enter the book title:")
            if st.button("Search"):
                results = [book for book in books_library if book["title"].lower() == search_title.lower()]
                if results:
                    st.write(f"Found {len(results)} book(s):")
                    for book in results:
                        st.write(book)
                else:
                    st.write("No books found.")

        elif search_method == "Author":
            search_author = st.text_input("Enter the author's name:")
            if st.button("Search"):
                results = [book for book in books_library if book["author"].lower() == search_author.lower()]
                if results:
                    st.write(f"Found {len(results)} book(s):")
                    for book in results:
                        st.write(book)
                else:
                    st.write("No books found.")

    # Display Statistics
    elif option == "Display Statistics":
        st.subheader("Statistics")
        total_books = len(books_library)
        read_books = sum(1 for book in books_library if book["read"].lower() == "yes")

        if total_books > 0:
            read_percentage = (read_books / total_books) * 100
            st.write(f"Total books: {total_books}")
            st.write(f"Books read: {read_books}")
            st.write(f"Percentage of books read: {read_percentage:.1f}%")
        else:
            st.write("No books in the library!")

    # Save & Exit
    elif option == "Save & Exit":
        save_library(books_library)
        st.success("Library saved to file. Goodbye!")

# Run the app
if __name__ == "__main__":
    personal_library_manager()

















# PURE PYTHON CODE HERE


# def Personal_Library_Manager():
#   print("Welcome to your Personal Library Manager!")
  
#   # Load library.txt books data from file.
#   with open("library.txt", "r") as file:
#     books_librbary = eval(file.read())
#     print(books_librbary)

#     # Books savings
#   books_librbary = []

#   while True:
#     print("""\n1. Add a book
# 2. Remove a book
# 3. Search for a book
# 4. Display all books
# 5. Display statistics
# 6. Exit
# """)




#     user_choice = int(input("Enter your choice: "))

#   # Book add
#     if user_choice == 1:
#       title = input("Enter the book title: ")
#       author = input("Enter the author: ")
#       publication = input("Enter the publication year: ")
#       genre = input("Enter the genre: ")
#       read = input("Have you read this book? (yes/no): ")

#       user_book = {
#           "title": title,
#           "author": author,
#           "publication": publication,
#           "genre": genre,
#           "read": read
#          }

#       books_librbary.append(user_book)
#       print("\n",books_librbary)
#       print("Book added successfully!")


#     # Remove a book
#     elif user_choice == 2:
#       remove_book = input("Enter the title of the book to remove: ")

#       for obj_book in books_librbary:
#         if obj_book["title"] == remove_book:
#           books_librbary.remove(obj_book)
#           print(f"Book deleted Successfully {obj_book}")



#     # Search book
#     elif user_choice == 3:
#       print("Search by:")     
#       print("1. Title:")     
#       print("2. Author:") 

#       search_method = int(input("Enter your Choice: "))

#       if search_method == 1:
#         search_by_title = input("Enter the title: ")
#         for obj in books_librbary:
#           if obj["title"] == search_by_title:
#             print(f"Your Search Book is: {obj}")

#       elif search_method == 2:
#         search_by_author = input("Enter Author name: ") 
#         for auth_obj in books_librbary:
#           if auth_obj["author"] == search_by_author:
#             print(f"Your Search Book is: {auth_obj}")


#       # Display All books
#     elif user_choice == 4:
#       print("Your Library")
#       for index , book in enumerate(books_librbary):
#         print(f"{index +1}. {book}")


#     # Display Statistics
#     elif user_choice == 5:
#       total = len(books_librbary)
#       print("Total books: ", total) 

#       read_books = sum(1   for book in books_librbary   if book["read"].lower() == "yes")


#       if total > 0:
#         read_percentage = (read_books / total) * 100
#         print(f"Percentage read: {read_percentage:.1f}%")

#       else:
#         print("No Books in the Library!d")  

     
#     # for exit  
#     elif user_choice == 6:
        
#         with open("library.txt", "w") as file:
#             file.write(str(books_librbary))
        
#         print("Library saved to file. Goodbye!")
#         break



# Personal_Library_Manager()



# # Writing to a file (this will overwrite if the file exists)
# with open("file.txt", "w") as file:
#     file.write("Hello, Python!")