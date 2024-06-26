import sqlite3
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QMessageBox,
    QTableWidgetItem
)
from mainwindow_v2 import Ui_MainWindow
from addbook import addBookDialog
from rentbook import RentBookDialog
from editbook import editbookDialog
from addcustomer import addCustomerDialog
from editcustomer import editCustomerDialog

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        try:
            # Initialize the UI from a separate UI file
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)

            # Connect UI elements to class variables
            self.homebutton = self.ui.homebutton
            self.bookbutton = self.ui.bookbutton
            self.customerbutton = self.ui.customerbutton
            self.stackedWidget = self.ui.stackedWidget
            self.booktable = self.ui.booktable
            self.customertable = self.ui.customertable

            # Connect button click events to methods
            self.homebutton.clicked.connect(self.show_home)
            self.bookbutton.clicked.connect(self.show_books)
            self.customerbutton.clicked.connect(self.show_customers)

            # Connect the Add Book button to the addBookDialog slot
            self.ui.addbookbtn.clicked.connect(self.add_book_dialog)
            self.ui.addcustomerbtn.clicked.connect(self.add_customer_dialog)
            self.ui.rentbtn.clicked.connect(self.rent_book_dialog)
            self.ui.updatebookbtn.clicked.connect(self.update_book_dialog)
            self.ui.updatecustomerbtn.clicked.connect(self.update_customer_dialog)

            # Initialize the UI
            self.show_home()

            # Initialize the database
            self.init_database()
            # Load books and customers
            self.load_books()
            self.load_customers()
        except Exception as e:
            print("An error occurred:", e)

    def show_home(self):
        # Set the current index of the stacked widget to show the home page
        self.stackedWidget.setCurrentIndex(0)

    def show_books(self):
        # Set the current index of the stacked widget to show the books page
        self.stackedWidget.setCurrentIndex(1)

    def show_customers(self):
        # Set the current index of the stacked widget to show the customers page
        self.stackedWidget.setCurrentIndex(2)

    # functionalities under book page
    def add_book_dialog(self):
        # Instantiate the Add Book dialog
        dialog = QtWidgets.QDialog()
        try:       
            ui = addBookDialog()
            ui.setupUi(dialog)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                book_info = ui.get_book_info()
                self.add_book_to_db(book_info)
        except Exception as e:
            print("Error occurred:", e)
    
    def update_book_dialog(self):
        try:
            # Instantiate the Add Book dialog
            dialog = QtWidgets.QDialog()
            ui = editbookDialog()
            ui.setupUi(dialog)
            dialog.exec()
        except Exception as e:
            print("Error occurred:", e)

    # functionalities under home tab
    def rent_book_dialog(self):
        try:
            dialog = QtWidgets.QDialog()
            ui = RentBookDialog()
            ui.setupUi(dialog)
            dialog.exec()
        except Exception as e:
            print("Error occurred:", e)

    # functionalities under customer tab
    def add_customer_dialog(self):
        try:
            dialog = QtWidgets.QDialog()
            ui = addCustomerDialog()
            ui.setupUi(dialog)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                customer_info = ui.get_customer_info()
                self.add_customer_to_db(customer_info)
        except Exception as e:
            print("Error occurred:", e)

    def update_customer_dialog(self):
        try:
            dialog = QtWidgets.QDialog()
            ui = editCustomerDialog()
            ui.setupUi(dialog)
            dialog.exec()
        except Exception as e:
            print("Error occurred:", e)


    # creating db
    def init_database(self):
        try:
            # Connect to the SQLite database (or create it if it doesn't exist)
            conn = sqlite3.connect('library.db')
            c = conn.cursor()

            # Create the customers table
            c.execute('''CREATE TABLE IF NOT EXISTS customers
                         (CustomerID TEXT PRIMARY KEY,
                          Name TEXT,
                          Gender TEXT,
                          PhoneNumber TEXT,
                          ValidIdPath TEXT)''')

            # Create the books table
            c.execute('''CREATE TABLE IF NOT EXISTS books
                         (BookID INTEGER PRIMARY KEY AUTOINCREMENT,
                          ISBN INTEGER,
                          Title TEXT,
                          Author TEXT, 
                          Category TEXT,
                          Status TEXT,
                          RentalFee INTEGER, 
                          Description TEXT,
                          Cover_Image TEXT)''')

            # Create the rentals table
            c.execute('''CREATE TABLE IF NOT EXISTS rentals
                         (CustomerId TEXT,
                          BookID INTEGER,
                          RentalDate TEXT,
                          RentalDueDate TEXT,
                          RentalFee INTEGER,
                          FOREIGN KEY (CustomerId) REFERENCES customers(CustomerID),
                          FOREIGN KEY (BookID) REFERENCES books(BookID))''')

            # Create the returns table
            c.execute('''CREATE TABLE IF NOT EXISTS returns
                         (CustomerId TEXT,
                          BookID INTEGER,
                          ReturnDate TEXT,
                          RentalDueDate TEXT,
                          OverdueFee INTEGER,
                          FOREIGN KEY (CustomerId) REFERENCES customers(CustomerID),
                          FOREIGN KEY (BookID) REFERENCES books(BookID),
                          FOREIGN KEY (RentalDueDate) REFERENCES rentals(RentalDueDate))''')

            # Create the reserve table
            c.execute('''CREATE TABLE IF NOT EXISTS reserve
                         (CustomerId TEXT,
                          BookID INTEGER,
                          ReservationDate TEXT,
                          ReservationFee REAL,
                          FOREIGN KEY (CustomerId) REFERENCES customers(CustomerID),
                          FOREIGN KEY (BookID) REFERENCES books(BookID))''')

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("An error occurred while initializing the database:", e)

    # loading db contents to book tableview
    def load_books(self):
        try:
            # Connect to the database
            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()

            # Fetch all books from the books table
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()

            # Clear the existing items in the book table
            self.booktable.clearContents()
            self.booktable.setRowCount(0)

            # Iterate over the fetched books and populate the table
            for row_number, book in enumerate(books):
                self.booktable.insertRow(row_number)
                for column_number, data in enumerate(book):
                    item = QTableWidgetItem(str(data))
                    self.booktable.setItem(row_number, column_number, item)

            # Close the database connection
            conn.close()
        except sqlite3.Error as e:
            print("An error occurred while loading books:", e)

    # loading db contents to customer tableview
    def load_customers(self):
        try:
            # Connect to the database
            conn = sqlite3.connect('library.db')
            cursor = conn.cursor()

            # Fetch all customers from the customers table
            cursor.execute("SELECT * FROM customers")
            customers = cursor.fetchall()

            # Clear the existing items in the customer table
            self.customertable.clearContents()
            self.customertable.setRowCount(0)

            # Iterate over the fetched customers and populate the table
            for row_number, customer in enumerate(customers):
                self.customertable.insertRow(row_number)
                for column_number, data in enumerate(customer):
                    item = QTableWidgetItem(str(data))
                    self.customertable.setItem(row_number, column_number, item)

            # Close the database connection
            conn.close()
        except sqlite3.Error as e:
            print("An error occurred while loading customers:", e)

    # Method to add a new book to the database
    def add_book_to_db(self, book_info):
        try:
            with sqlite3.connect("library.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO books (ISBN, Title, Author, Category, Status, RentalFee, Description, Cover_Image) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    book_info)
                conn.commit()
                
            self.load_books()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Error adding book: {e}")
    
    # Method to add a new customer to the database
    def add_customer_to_db(self, customer_info):
        try:
            with sqlite3.connect("library.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO customers (Name, Gender, PhoneNumber, ValidIdPath) VALUES (?, ?, ?, ?)",
                    customer_info
                )
                conn.commit()

            self.load_customers()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Error", f"Error adding customer: {e}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

