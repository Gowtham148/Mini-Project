
# Importing the PySimpleGUI for simple User Interface to make the application look good
# Importing the sqlite3 to maintain the database of the customers and the books

import sqlite3
import PySimpleGUI as sg

# Function that asks the user whether he/she is a customer or a librarian
# This function specifies the window that the user first sees in the application


def first_page():

    sg.theme('Dark Blue 3')
    layout = [[sg.Text('Are you a Librarian or a Customer')],
              [sg.Button('Librarian'), sg.Button('Customer')]]

    window = sg.Window('Welcome to the Library', layout)

    event, values = window.read()

    sg.Popup(event)

    window.close()

# Creating the required databases for the application
# The tables in this database are Customer, Book and Info


def creating_database():
    conn = sqlite3.connect("Library.db")
    
    c = conn.cursor()
    
    c.execute("""CREATE TABLE IF NOT EXISTS Book( 
                       BId INT PRIMARY KEY, 
                       BName VARCHAR(50) NOT NULL, 
                       Author VARCHAR(50) NOT NULL, 
                       Qty INT, 
                       Price DOUBLE );""")

    c.execute("""CREATE TABLE IF NOT EXISTS Customer(
                       CId INT PRIMARY KEY, 
                       BId INT REFERENCES Book(BId), 
                       Name VARCHAR(50) NOT NULL, 
                       Age INT,
                       Password VARCHAR(50));""")

    c.execute("""CREATE TABLE IF NOT EXISTS Info(
                       BId INT REFERENCES Book(BId),
                       CId INT REFERENCES Customer(CId),
                       BDate DATE NOT NULL,
                       RDate DATE NOT NULL,
                       Due_Amount DOUBLE  );""")
    conn.commit()

    conn.close()


# Inserting the necessary values into the tables


def insert_into_books():
    conn = sqlite3.connect("Library.db")

    c = conn.cursor()
    
    c.execute("INSERT INTO Book VALUES(1,'For whom the Bell tolls','Ernest Hemingway',10,750);")
    c.execute("INSERT INTO Book VALUES(2,'Kurukku','Faustima Bama',10,400);")
    c.execute("INSERT INTO Book VALUES(3,'Shah Nama','Firdausi',5,300);")
    c.execute("INSERT INTO Book VALUES(4,'The Castle','Franz kalka',7,300);")
    c.execute("INSERT INTO Book VALUES(5,'Apple Cart','G.B Shaw',4,600);")
    c.execute("INSERT INTO Book VALUES(6,'Man and Superman','G.B Shaw',7,450);")
    c.execute("INSERT INTO Book VALUES(7,'All about H. Hatterr','G.v Desani',7,450);")
    c.execute("INSERT INTO Book VALUES(8,'Arms and the Man','G.b Shaw',3,550);")
    c.execute("INSERT INTO Book VALUES(9,'Kanterbury Tells','Geofray Chosar',2,480);")
    c.execute("INSERT INTO Book VALUES(10,'Silas Marnar','George Eliot',6,550);")
    c.execute("INSERT INTO Book VALUES(11,'Animal Farm','George Orwell',10,400);")
    c.execute("INSERT INTO Book VALUES(12,'1984','George Orwell',10,400);")
    c.execute("INSERT INTO Book VALUES(13,'Tughlaq','Girish Karnad',13,500);")
    c.execute("INSERT INTO Book VALUES(14,'faust','Goethe',2,300);")
    c.execute("INSERT INTO Book VALUES(15,'Paraja','Gopinath Mohanty',2,250);")
    c.execute("INSERT INTO Book VALUES(16,'She walk,she leads','Gunjan Jain',9,550);")
    c.execute("INSERT INTO Book VALUES(17,'Asian Drama','Gunnar Myrdal',3,290);")
    c.execute("INSERT INTO Book VALUES(18,'A Womans life','Guy de maupassaut',12,400);")
    c.execute("INSERT INTO Book VALUES(19,'Time Machine','H G Wells',2,200);")
    c.execute("INSERT INTO Book VALUES(20,'Invisible Man','H G Wells',1,230);")

    conn.commit()

    conn.close()


# Inserting into the customers table

def insert_into_customers():
    conn = sqlite3.connect("Library.db")

    c = conn.cursor()

    c.execute("INSERT INTO Customer VALUES(1,10,'Gowtham',21,'gowtham10');")
    c.execute("INSERT INTO Customer VALUES(2,18,'Vaidehi',16,'vaidehi10')")

    conn.commit()

    conn.close()


# Test statement - Might delete later

def select():
    conn = sqlite3.connect("Library.db")

    c = conn.cursor()
    c.execute("SELECT Customer.Name,Book.BName FROM Customer,Book WHERE Book.BId = Customer.BId;")
    print(c.fetchall())

    conn.commit()
    conn.close()


""" Function Calls / the main program
    Sort of like the main program - (I'm from C++)  
"""

creating_database()
insert_into_books()
insert_into_customers()
first_page()
select()
