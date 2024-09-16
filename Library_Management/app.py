import streamlit as st
from PIL import Image  # To load images

# Initialize global variables
if 'librarians' not in st.session_state:
    st.session_state.librarians = []

if 'books' not in st.session_state:
    st.session_state.books = []

if 'lend_list' not in st.session_state:
    st.session_state.lend_list = []

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'current_user' not in st.session_state:
    st.session_state.current_user = ""

# Helper function to display alert messages in Streamlit
def show_message(title, message, alert_type='info'):
    if alert_type == 'error':
        st.error(message)
    else:
        st.success(message)

# Function to handle login
def login(username, password):
    for librarian in st.session_state.librarians:
        if username == librarian[0] and password == librarian[1]:
            st.session_state.logged_in = True
            st.session_state.current_user = username
            return True
    return False

# Function to handle registration
def register(username, password):
    st.session_state.librarians.append([username, password])
    show_message("Success", "Registration successful!")

# Function to add a book
def add_book(book_name):
    st.session_state.books.append(book_name)
    show_message("Success", "Book added successfully!")

# Function to remove a book
def remove_book(book_name):
    if book_name in st.session_state.books:
        st.session_state.books.remove(book_name)
        show_message("Success", "Book removed successfully!")
    else:
        show_message("Error", "Book not found", alert_type='error')

# Function to issue a book
def issue_book(book_name):
    if book_name in st.session_state.books:
        st.session_state.lend_list.append(book_name)
        st.session_state.books.remove(book_name)
        show_message("Success", "Book issued successfully!")
    else:
        show_message("Error", "Book not found", alert_type='error')

# Function to display available books
def view_books():
    if st.session_state.books:
        st.write("Available Books:")
        for book in st.session_state.books:
            st.write(f"- {book}")
    else:
        st.write("No books available.")

# UI: Library management system
def library_management_ui():
    st.header(f"Welcome, {st.session_state.current_user}")

    # Add a library logo or welcome image at the top
    library_logo = Image.open("images/Library_Logo.jpg")
    st.image(library_logo, use_column_width=True)

    # Add book section
    st.subheader("Add Book")
    book_name = st.text_input("Enter book name to add:")
    if st.button("Add Book"):
        if book_name:
            add_book(book_name)

    # Remove book section
    st.subheader("Remove Book")
    book_to_remove = st.text_input("Enter book name to remove:")
    if st.button("Remove Book"):
        if book_to_remove:
            remove_book(book_to_remove)

    # Issue book section
    st.subheader("Issue Book")
    book_to_issue = st.text_input("Enter book name to issue:")
    if st.button("Issue Book"):
        if book_to_issue:
            issue_book(book_to_issue)

    # View books section
    st.subheader("View Books")
    if st.button("View Available Books"):
        view_books()

# Main screen
def main():
    st.title("Library Management System")

    # Display a welcome image on the login screen
    welcome_image = Image.open("images/Library_Background.jpg")
    st.image(welcome_image, use_column_width=True)

    if not st.session_state.logged_in:
        st.subheader("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login"):
            if login(username, password):
                st.experimental_rerun()  # Re-run app after login
            else:
                show_message("Error", "Invalid username or password", alert_type='error')

        st.subheader("Register")
        new_username = st.text_input("New Username")
        new_password = st.text_input("New Password", type="password")
        
        if st.button("Register"):
            if new_username and new_password:
                register(new_username, new_password)
            else:
                show_message("Error", "Username and Password are required", alert_type='error')
    else:
        library_management_ui()

if __name__ == "__main__":
    main()
