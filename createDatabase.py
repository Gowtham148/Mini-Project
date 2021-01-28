# Importing the libraries
import sqlite3


def create_database():
    connection = sqlite3.connect("Library.db")
    connection.close()


def create_book_table():
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Book( 
                        BId INT PRIMARY KEY, 
                        BName VARCHAR(50) NOT NULL, 
                        Author VARCHAR(50) NOT NULL, 
                        Qty INT, 
                        Price DOUBLE );""")
    connection.commit()
    connection.close()


def create_customer_table():
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Customer(
                       CId INT PRIMARY KEY,  
                       Name VARCHAR(50) NOT NULL, 
                       Age INT,
                       Sex VARCHAR(2),
                       City VARCHAR(20),
                       Password VARCHAR(50));""")
    connection.commit()
    connection.close()


def create_librarian_table():
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS Librarian(
                       LId INT PRIMARY KEY,
                       Name VARCHAR(50) NOT NULL,
                       Age INT,
                       Sex VARCHAR(2),
                       City VARCHAR(20),
                       Password VARCHAR(50));""")
    connection.commit()
    connection.close()
