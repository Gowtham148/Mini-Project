# Importing the required libraries
import sqlite3


def check_customer(name, password):
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    c.execute("SELECT Name, Password FROM Customer;")
    variable = c.fetchall()

    for i, j in variable:
        if i == name and j == password:
            connection.close()
            return True

    connection.close()
    return False


def check_librarian(name, password):
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    c.execute("SELECT Name, Password FROM Librarian;")
    variable = c.fetchall()

    for i, j in variable:
        if i == name and j == password:
            connection.close()
            return True

    connection.close()
    return False


def book_exists(name, author):
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    c.execute("SELECT BName, Author FROM Book;")
    variable = c.fetchall()

    for i, j in variable:
        if i == name and j == author:
            connection.close()
            return True

    connection.close()
    return False


def find_librarian(name, age, city):
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    c.execute('SELECT Name, Age, City FROM Librarian;')
    variable = c.fetchall()
    connection.commit()
    connection.close()

    for i, j, k in variable:
        if i == name and j == age and k == city:
            return True

    return False


def check_password(password, cpassword):
    if password == cpassword:
        return True

    return False
