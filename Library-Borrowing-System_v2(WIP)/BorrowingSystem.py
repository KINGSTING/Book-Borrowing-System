import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QLineEdit,
    QMessageBox,
    QListWidget,
    QDialog,
    QComboBox,
    QTextEdit,
    QTabWidget,
    QDialogButtonBox,
    QFormLayout,
    QFileDialog
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
import sqlite3


# Dialog for adding a new book
class AddBookDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Book")
        layout = QVBoxLayout(self)

        # Input fields for author, title, category, description, and fee
        self.ISBN_input = QLineEdit(self)
        self.ISBN_input.setPlaceholderText("Enter ISBN code")
        layout.addWidget(self.ISBN_input)

        self.author_input = QLineEdit(self)
        self.author_input.setPlaceholderText("Enter author")
        layout.addWidget(self.author_input)

        self.title_input = QLineEdit(self)
        self.title_input.setPlaceholderText("Enter title")
        layout.addWidget(self.title_input)

        layout.addWidget(QLabel("Category:"))
        category_layout = QVBoxLayout()
        layout.addLayout(category_layout)

        genres = [
            "Action", "Adventure", "Anthology", "Art",
            "Biography", "Business",
            "Children's", "Classics", "Comedy", "Comics", "Contemporary", "Cookbooks", "Crime",
            "Drama", "Dystopian",
            "Economics", "Education", "Epic", "Essays",
            "Fairy Tale", "Fantasy", "Fiction", "Folklore",
            "Graphic Novels", "Gothic",
            "Historical Fiction", "History", "Horror", "Humor",
            "Inspirational", "Instructional",
            "Journalism",
            "Kids", "Knowledge",
            "Literary Fiction", "Literature",
            "Memoir", "Mystery", "Mythology",
            "Non-fiction",
            "Occult", "Outdoors",
            "Paranormal", "Philosophy", "Photography", "Poetry", "Political", "Psychology",
            "Queer Literature",
            "Realistic Fiction", "Reference", "Religion", "Romance",
            "Satire", "Science", "Science Fiction", "Self-help", "Short Stories", "Spiritual", "Sports", "Suspense",
            "Technology", "Thriller", "Travel", "True Crime",
            "Urban Fantasy",
            "Vampire", "Veterinary",
            "War", "Western",
            "Young Adult",
            "Zombie"
        ]

        self.category_combo = QComboBox(self)
        self.category_combo.addItems(genres)
        category_layout.addWidget(self.category_combo)

        self.description_input = QTextEdit(self)
        self.description_input.setPlaceholderText("Enter description")
        layout.addWidget(self.description_input)

        self.fee_input = QLineEdit(self)
        self.fee_input.setPlaceholderText("Enter fee")
        layout.addWidget(self.fee_input)

        self.cover_image_button = QPushButton("Select Cover Image")
        self.cover_image_button.clicked.connect(self.select_cover_image)
        layout.addWidget(self.cover_image_button)

        self.cover_image_label = QLabel("No image selected")
        layout.addWidget(self.cover_image_label)

        # Buttons for adding and canceling
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(buttons)

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

    # Method to select an image for the book cover
    def select_cover_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Cover Image", "",
                                                   "Images (*.png *.xpm *.jpg);;All Files (*)")
        if file_name:
            self.cover_image_label.setText(file_name)

    # Method to get the entered book information
    def get_book_info(self):
        BookId = self.ISBN_input.text()
        Title = self.title_input.text()
        Author = self.author_input.text()
        Category = self.category_combo.currentText()
        Status = "Available"
        Description = self.description_input.toPlainText()
        Cover_image = self.cover_image_label.text()
        try:
            Rentalfee = float(self.fee_input.text())
        except ValueError:
            Rentalfee = 0.0
        return BookId, Title, Author, Category, Status, Description, Rentalfee, Cover_image


# Dialog for adding a new customer
class AddCustomerDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Customer")
        layout = QVBoxLayout(self)

        # Input fields for customer information
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter name")
        layout.addWidget(self.name_input)

        self.gender_combo = QComboBox(self)
        self.gender_combo.addItems(["Male", "Female", "Other"])
        layout.addWidget(self.gender_combo)

        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Enter phone number")
        layout.addWidget(self.phone_input)

        self.valid_id_button = QPushButton("Select Valid ID Image")
        self.valid_id_button.clicked.connect(self.select_valid_id_image)
        layout.addWidget(self.valid_id_button)

        self.valid_id_label = QLabel("No image selected")
        layout.addWidget(self.valid_id_label)

        # Buttons for adding and canceling
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        layout.addWidget(buttons)

        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)

    # Method to select an image for the valid ID
    def select_valid_id_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Valid ID Image", "",
                                                   "Images (*.png *.xpm *.jpg);;All Files (*)")
        if file_name:
            self.valid_id_label.setText(file_name)

    # Method to get the entered customer information
    def get_customer_info(self):
        CustomerId = self.generate_customer_id()
        Name = self.name_input.text()
        Gender = self.gender_combo.currentText()
        PhoneNumber = self.phone_input.text()
        ValidIdPath = self.valid_id_label.text()
        return CustomerId, Name, Gender, PhoneNumber, ValidIdPath

    def generate_customer_id(self):
        try:
            with sqlite3.connect("library.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT CustomerId FROM customers ORDER BY CustomerId DESC LIMIT 1")
                result = cursor.fetchone()
                if result:
                    last_id = result[0]
                    # Extract the numeric part, increment it, and format back to Axx
                    numeric_part = int(last_id[1:])
                    new_numeric_part = numeric_part + 1
                    new_id = f"A{new_numeric_part:02d}"
                else:
                    # No existing IDs, start with A01
                    new_id = "A01"
                return new_id
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Error generating customer ID: {e}")
            return None


# Dialog for displaying detailed book information
class BookInfoDialog(QDialog):
    def __init__(self, book_info):
        super().__init__()
        self.setWindowTitle("Book Details")
        layout = QVBoxLayout(self)

        self.book_info = book_info

        # Form layout to display book details
        form_layout = QFormLayout()

        for key, value in book_info.items():
            label = QLabel(key)
            form_layout.addRow(label, QLabel(str(value)))

        layout.addLayout(form_layout)

        # Button for closing the dialog
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        layout.addWidget(buttons)

        buttons.accepted.connect(self.accept)

    # Method to handle renting a book
    def rent_book(self):
        selected_customer = self.customer_combo.currentText()
        if selected_customer:
            return selected_customer
        else:
            QMessageBox.warning(self, "Warning", "Please select a customer.")
            return None


# Dialog for displaying detailed customer information
# Dialog for displaying detailed customer information
class CustomerInfoDialog(QDialog):
    def __init__(self, customer_info):
        super().__init__()
        self.setWindowTitle("Customer Details")
        layout = QVBoxLayout(self)

        # Form layout to display customer details
        form_layout = QFormLayout()

        for key, value in customer_info.items():
            if key != "Valid ID":
                label = QLabel(key)
                form_layout.addRow(label, QLabel(str(value)))
            else:
                label = QLabel(key)
                image_label = QLabel(self)
                pixmap = QPixmap(value)
                image_label.setPixmap(pixmap.scaled(200, 200, Qt.AspectRatioMode.KeepAspectRatio))
                form_layout.addRow(label, image_label)

        layout.addLayout(form_layout)

        # Button for closing the dialog
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        layout.addWidget(buttons)

        buttons.accepted.connect(self.accept)


# Main application window
class LibraryApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Book Rental System")
        self.setGeometry(100, 100, 500, 400)
        self.setWindowIcon(QIcon('icon.png'))  # Optional: Set an application icon

        self.init_ui()
        self.init_database()

        self.load_books()
        self.load_customers()

    def init_database(self):
        conn = sqlite3.connect("library.db")
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS customers
                         (CustomerId TEXT PRIMARY KEY,
                          Name TEXT,
                          Gender TEXT,
                          PhoneNumber TEXT,
                          ValidIdPath)''')
        c.execute('''CREATE TABLE IF NOT EXISTS books
                        (BookId TEXT PRIMARY KEY,
                         Title TEXT,
                         Author TEXT, 
                         Category TEXT,
                         Status TEXT,
                         RentalFee INTEGER, 
                         Description TEXT,
                         Cover_Image TEXT)''')
        c.execute('''CREATE TABLE IF NOT EXISTS rentals
                        (CustomerId TEXT,
                         BookId TEXT,
                         RentalDate TEXT,
                         RentalDueDate TEXT,
                         RentalFee INTEGER,
                         FOREIGN KEY (CustomerId) REFERENCES customers(CustomerId),
                         FOREIGN KEY (BookId) REFERENCES books(BookCode))''')

        c.execute('''CREATE TABLE IF NOT EXISTS returns
                        (CustomerId TEXT,
                         BookId TEXT,
                         ReturnDate TEXT,
                         RentalDueDate TEXT,
                         OverdueFee INTEGER,
                         FOREIGN KEY (CustomerId) REFERENCES customers(CustomerId),
                         FOREIGN KEY (BookId) REFERENCES books(BookCode),
                         FOREIGN KEY (RentalDueDate) REFERENCES rentals(RentalDueDate))''')

        c.execute('''CREATE TABLE IF NOT EXISTS reserve
                        (CustomerId TEXT,
                         BookId TEXT,
                         ReservationDate TEXT,
                         ReservationFee REAL,
                         FOREIGN KEY (CustomerId) REFERENCES customers(CustomerId),
                         FOREIGN KEY (BookId) REFERENCES books(BookCode))''')

        conn.commit()
        conn.close()

    # Method to initialize the UI
    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Tab widget to manage books and customers
        tab_widget = QTabWidget(self)
        layout.addWidget(tab_widget)

        # Tab for managing books
        book_tab = QWidget(self)
        tab_widget.addTab(book_tab, "Books")
        book_tab_layout = QVBoxLayout(book_tab)

        # Title label for book tab
        title_label = QLabel("Book Rental System - Books", self)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 18pt; font-weight: bold;")
        book_tab_layout.addWidget(title_label)

        # Button for adding a new book
        button_layout = QHBoxLayout()
        add_book_button = QPushButton("Add Book", self)
        add_book_button.setToolTip("Add a new book to the library")
        add_book_button.clicked.connect(self.show_add_book_dialog)
        self.set_button_style(add_book_button)
        button_layout.addWidget(add_book_button)
        book_tab_layout.addLayout(button_layout)

        # Filter input for searching books
        filter_layout = QHBoxLayout()
        filter_label = QLabel("Filter books by:", self)
        filter_layout.addWidget(filter_label)
        self.filter_type_combo = QComboBox(self)
        self.filter_type_combo.addItems(["Title", "Author", "Category"])
        filter_layout.addWidget(self.filter_type_combo)
        self.filter_input = QLineEdit(self)
        self.filter_input.setPlaceholderText("Enter filter text")
        filter_layout.addWidget(self.filter_input)
        filter_button = QPushButton("Filter", self)
        filter_button.clicked.connect(self.filter_books)
        filter_layout.addWidget(filter_button)
        book_tab_layout.addLayout(filter_layout)

        # List to display books
        self.books_list = QListWidget(self)
        book_tab_layout.addWidget(self.books_list)

        # Buttons for viewing more info and removing books
        books_button_layout = QHBoxLayout()
        book_tab_layout.addLayout(books_button_layout)
        more_info_button = QPushButton("More Info", self)
        more_info_button.setToolTip("View more information about the selected book")
        more_info_button.clicked.connect(self.show_book_info)
        self.set_button_style(more_info_button)
        books_button_layout.addWidget(more_info_button)

        remove_book_button = QPushButton("Remove Book", self)
        remove_book_button.setToolTip("Remove the selected book from the library")
        remove_book_button.clicked.connect(self.remove_book)
        self.set_button_style(remove_book_button)
        books_button_layout.addWidget(remove_book_button)

        # Tab for managing customers
        customer_tab = QWidget(self)
        tab_widget.addTab(customer_tab, "Customers")
        customer_tab_layout = QVBoxLayout(customer_tab)

        # Title label for customer tab
        title_label = QLabel("Book Rental System - Customers", self)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 18pt; font-weight: bold;")
        customer_tab_layout.addWidget(title_label)

        # Button for adding a new customer
        button_layout = QHBoxLayout()
        add_customer_button = QPushButton("Add Customer", self)
        add_customer_button.setToolTip("Add a new customer to the system")
        add_customer_button.clicked.connect(self.show_add_customer_dialog)
        self.set_button_style(add_customer_button)
        button_layout.addWidget(add_customer_button)
        customer_tab_layout.addLayout(button_layout)

        # Filter input for searching customers
        filter_layout = QHBoxLayout()
        filter_label = QLabel("Filter customers by:", self)
        filter_layout.addWidget(filter_label)
        self.filter_customer_type_combo = QComboBox(self)
        self.filter_customer_type_combo.addItems(["Name", "Number"])
        filter_layout.addWidget(self.filter_customer_type_combo)
        self.filter_customer_input = QLineEdit(self)
        self.filter_customer_input.setPlaceholderText("Enter filter text")
        filter_layout.addWidget(self.filter_customer_input)
        filter_button = QPushButton("Filter", self)
        filter_button.clicked.connect(self.filter_customers)
        filter_layout.addWidget(filter_button)
        customer_tab_layout.addLayout(filter_layout)

        # List to display customers
        self.customers_list = QListWidget(self)
        customer_tab_layout.addWidget(self.customers_list)

        # Buttons for viewing more info and removing customers
        customers_button_layout = QHBoxLayout()
        customer_tab_layout.addLayout(customers_button_layout)
        more_info_button = QPushButton("More Info", self)
        more_info_button.setToolTip("View more information about the selected customer")
        more_info_button.clicked.connect(self.show_customer_info)
        self.set_button_style(more_info_button)
        customers_button_layout.addWidget(more_info_button)

        remove_customer_button = QPushButton("Remove Customer", self)
        remove_customer_button.setToolTip("Remove the selected customer from the system")
        remove_customer_button.clicked.connect(self.remove_customer)
        self.set_button_style(remove_customer_button)
        customers_button_layout.addWidget(remove_customer_button)

    # Method to set consistent style for buttons
    def set_button_style(self, button):
        button.setStyleSheet("font-size: 14pt; padding: 10px;")

    # Method to show the dialog for adding a new book
    def show_add_book_dialog(self):
        dialog = AddBookDialog()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            book_info = dialog.get_book_info()
            self.add_book_to_db(book_info)
            self.load_books()

    # Method to show the dialog for adding a new customer
    def show_add_customer_dialog(self):
        dialog = AddCustomerDialog()
        if dialog.exec() == QDialog.DialogCode.Accepted:
            customer_info = dialog.get_customer_info()
            self.add_customer_to_db(customer_info)
            self.load_customers()

    # Method to filter books based on user input
    def filter_books(self):
        filter_type = self.filter_type_combo.currentText().lower()
        filter_text = self.filter_input.text()
        try:
            with sqlite3.connect("library.db") as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM books WHERE {filter_type} LIKE ?", (f"%{filter_text}%",))
                books = cursor.fetchall()
                self.books_list.clear()
                for book in books:
                    self.books_list.addItem(f"{book[2]} by {book[1]}")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Error filtering books: {e}")

    # Method to filter customers based on user input
    def filter_customers(self):
        filter_type = self.filter_customer_type_combo.currentText().lower()
        filter_text = self.filter_customer_input.text()
        try:
            with sqlite3.connect("library.db") as conn:
                cursor = conn.cursor()
                cursor.execute(f"SELECT * FROM customers WHERE {filter_type} LIKE ?", (f"%{filter_text}%",))
                customers = cursor.fetchall()
                self.customers_list.clear()
                for customer in customers:
                    self.customers_list.addItem(f"{customer[1]} ({customer[2]})")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Error filtering customers: {e}")

    def show_book_info(self):
        selected_book = self.books_list.currentItem()
        if selected_book:
            book_title = selected_book.text().strip()  # Trim whitespace from book title
            print("Selected Book Title:", book_title)  # Debugging: Print selected book title
            try:
                conn = sqlite3.connect("library.db")
                cursor = conn.cursor()

                # Check if book_title exists in the Title column of the books table (case-insensitive comparison)
                cursor.execute("SELECT Title FROM books WHERE LOWER(Title) = LOWER(?)", (book_title,))
                existing_title = cursor.fetchone()
                print("Existing Title:", existing_title)  # Debugging: Print existing title

                if existing_title:
                    # Book title exists in the table
                    print("Book title exists in the books table.")

                    # Now fetch the book details
                    cursor.execute("SELECT * FROM books WHERE Title = ?", (existing_title[0],))
                    book_info = cursor.fetchone()

                    if book_info:
                        book_details = {
                            "BookId": book_info[0],
                            "Title": book_info[1],
                            "Author": book_info[2],
                            "Category": book_info[3],
                            "Status": book_info[4],
                            "RentalFee": book_info[5],
                            "Description": book_info[6],
                            "Cover_Image": book_info[7]
                        }
                        print("Book details:", book_details)
                        # Display book details in a dialog
                        dialog = BookInfoDialog(book_details)
                        dialog.exec()
                    else:
                        QMessageBox.warning(self, "Warning", "No book details found.")
                else:
                    # Book title does not exist in the table
                    print("Book title does not exist in the books table.")
                    QMessageBox.warning(self, "Warning", "Selected book not found in the database.")

            except sqlite3.Error as e:
                print("Error:", e)  # Debugging: Print SQLite error
                QMessageBox.critical(self, "Error", f"Error fetching book details: {e}")
            finally:
                conn.close()
        else:
            QMessageBox.warning(self, "Warning", "Please select a book to view details.")

    # Method to show detailed information about a selected customer
    def show_customer_info(self):
        selected_items = self.customers_list.selectedItems()
        if selected_items:
            selected_customer = selected_items[0].text().strip()
            print("Selected Customer:", selected_customer)  # Debugging: Print selected customer name
            try:
                conn = sqlite3.connect("library.db")
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM customers WHERE Name = ?", (selected_customer,))
                customer = cursor.fetchone()
                print("Existing customer:", customer)  # Debugging: Print existing customer details

                if customer:
                    customer_info = {
                        "CustomerId": customer[0],
                        "Name": customer[1],
                        "Gender": customer[2],
                        "Phone Number": customer[3],
                        "Valid ID": customer[4]
                    }
                    print("Customer details:", customer_info)  # Debugging: Print customer details
                    dialog = CustomerInfoDialog(customer_info)
                    dialog.exec()
                else:
                    QMessageBox.warning(self, "Warning", "Customer details not found.")
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", f"Error fetching customer details: {e}")

    # Method to load books from the database
    def load_books(self):
        try:
            with sqlite3.connect("library.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM books")
                books = cursor.fetchall()
                self.books_list.clear()
                for book in books:
                    self.books_list.addItem(f"{book[1]} ")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Error loading books: {e}")

    # Method to load customers from the database
    def load_customers(self):
        try:
            with sqlite3.connect("library.db") as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM customers")
                customers = cursor.fetchall()
                self.customers_list.clear()
                for customer in customers:
                    self.customers_list.addItem(f"{customer[1]}")
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Error loading customers: {e}")

    # Method to add a new book to the database
    def add_book_to_db(self, book_info):
        try:
            with sqlite3.connect("library.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO books (BookId, Title, Author, Category, Status, Description, RentalFee, Cover_Image) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    book_info)
                conn.commit()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Error adding book: {e}")

    # Method to add a new customer to the database
    def add_customer_to_db(self, customer_info):
        try:
            with sqlite3.connect("library.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO customers (CustomerId, Name, Gender, PhoneNumber, ValidIdPath) VALUES (?, ?, ?, ?, ?)",
                    customer_info)
                conn.commit()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Error adding customer: {e}")

    # Method to remove a selected book from the database
    def remove_book(self):
        selected_items = self.books_list.selectedItems()
        if selected_items:
            selected_book = selected_items[0].text()
            try:
                with sqlite3.connect("library.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM books WHERE title = ?", (selected_book.split(' by ')[0],))
                    conn.commit()
                    self.load_books()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", f"Error removing book: {e}")

    # Method to remove a selected customer from the database
    def remove_customer(self):
        selected_items = self.customers_list.selectedItems()
        if selected_items:
            selected_customer = selected_items[0].text()
            try:
                with sqlite3.connect("library.db") as conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM customers WHERE name = ?", (selected_customer.split(' (')[0],))
                    conn.commit()
                    self.load_customers()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Error", f"Error removing customer: {e}")


# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LibraryApp()
    window.show()
    sys.exit(app.exec())
