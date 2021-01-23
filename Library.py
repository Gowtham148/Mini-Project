
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

    sg.Popup('Taking you to the ' + event + ' Page')

    window.close()
    return event

# Creating the required databases for the application
# The tables in this database are Customer, Book and Info


def creating_database():
    conn = sqlite3.connect("Library.db")
    
    c = conn.cursor()

# Creating a table for the Books available in the library
    c.execute("""CREATE TABLE IF NOT EXISTS Book( 
                       BId INT PRIMARY KEY, 
                       BName VARCHAR(50) NOT NULL, 
                       Author VARCHAR(50) NOT NULL, 
                       Qty INT, 
                       Price DOUBLE );""")

# A table for the existing customers and their informations
    c.execute("""CREATE TABLE IF NOT EXISTS Customer(
                       CId INT PRIMARY KEY,  
                       Name VARCHAR(50) NOT NULL, 
                       Age INT,
                       Password VARCHAR(50));""")

# A table for the dates when the books were lent and returned
    c.execute("""CREATE TABLE IF NOT EXISTS Info(
                       BId INT REFERENCES Book(BId),
                       CId INT REFERENCES Customer(CId),
                       BDate DATE NOT NULL,
                       RDate DATE NOT NULL,
                       Due_Amount DOUBLE  );""")

# Table for the librarians
    c.execute("""CREATE TABLE IF NOT EXISTS Librarian(
                       LId INT PRIMARY KEY,
                       Name VARCHAR(50) NOT NULL,
                       Password VARCHAR(50));""")

    conn.commit()

    conn.close()


# Inserting the necessary values into the table Book
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

    c.execute("INSERT INTO Customer VALUES(1,'Gowtham',21,'gowtham10');")
    c.execute("INSERT INTO Customer VALUES(2,'Vaidehi',16,'vaidehi10')")

    conn.commit()

    conn.close()


# Inserting values into the Info table
def insert_into_info():
    conn = sqlite3.connect("Library.db")

    c = conn.cursor()

    c.execute("INSERT INTO Info VALUES(10,1,'20-05-2019','19-07-2019',0);")
    c.execute("INSERT INTO Info VALUES(17,2,'12-05-2018','25-08-2018',0);")

    conn.commit()

    conn.close()


# Inserting into the librarian table
def insert_into_librarian():
    conn = sqlite3.connect("Library.db")

    c = conn.cursor()

    c.execute("INSERT INTO Librarian VALUES(1,'Vasudevan','vasudevan10');")
    c.execute("INSERT INTO Librarian VALUES(2,'Gayathri','gayathri10');")

    conn.commit()
    conn.close()


# Checking if the entered information is valid / In the database
def check_info(name, password):
    conn = sqlite3.connect("Library.db")
    c = conn.cursor()

    c.execute("SELECT Name,Password FROM Customer;")

    temporary = c.fetchall()

    conn.commit()

    conn.close()

    for i, j in temporary:
        if i == name and j == password:
            return True

    return False


# Checking for the librarian information
def check(name, passw):
    conn = sqlite3.connect("Library.db")

    c = conn.cursor()

    c.execute("SELECT Name, Password FROM Librarian;")

    var = c.fetchall()

    conn.commit()

    conn.close()

    for i, j in var:
        if i == name and j == passw:
            return True

    return False


# This function is called when the user is a librarian
def librarian_page():
    layout = [[sg.Text('Welcome')],
              [sg.Text('Name'), sg.InputText(key = '-name-')],
              [sg.Text('Password'), sg.InputText(key = '-pass-')],
              [sg.Button('Sign In')]]

    window = sg.Window('Librarian Details',layout)

    event, values = window.read()

    if check(values['-name-'], values['-pass-']):
        window.close()
        return True

    else:
        window.close()
        return False


# Shows the customer page
def customer_page():
    layout = [[sg.Text('Welcome')],
              [sg.Text('Username: '), sg.InputText(key='-name-')],
              [sg.Text('Password: '), sg.InputText(key='-password-', password_char='*')],
              [sg.Button('Sign In')]]

    window = sg.Window('Librarian Details', layout)

    event, values = window.read()

    if check_info(values['-name-'], values['-password-']):
        print('Valid')
    else:
        print('Invalid')

    window.close()


"""
def select():
    conn = sqlite3.connect("Library.db")

    c = conn.cursor()

    c.execute("SELECT Name, Password FROM Customer;")

    var = c.fetchall()

    conn.commit()

    conn.close()

    print(var)
"""


# Creating a new customer and inserting the values into the database
def create_new_customer(name, age, password):
    conn = sqlite3.connect("Library.db")

    c = conn.cursor()

    c.execute("SELECT CId FROM Customer;")

    var = c.fetchall()

    number = len(var)
    number += 1
    query = "INSERT INTO Customer VALUES({num}, '{n}', {a}, '{p}');"
    query = query.format(num=number, n=name, a=age, p=password)
    print(query)

    c.execute(query)

    conn.commit()

    conn.close()

    sg.popup('New Customer added to the database')


# New Customer Information
def customer_info():
    layout = [[sg.Text('Name '), sg.InputText(key='-name-')],
                [sg.Text('Age '), sg.InputText(key='-age-')],
                [sg.Text('Type your password '), sg.InputText(key='-pass-')],
                [sg.Text('Confirm your password '), sg.InputText(key='-pass1-')],
                [sg.Button('Create User')]]

    window = sg.Window('Welcome!', layout)

    event, values = window.read()

    if values['-pass-'] != values['-pass1-']:
        sg.popup("Password doesn't match ")
    else:
        create_new_customer(values['-name-'], values['-age-'], values['-pass-'])

    window.close()


def customer_question():
    layout = [[sg.Text('Are you an existing customer?')],
              [sg.Button('Yes'), sg.Button('No')]]

    window = sg.Window('Welcome!', layout)

    event, values = window.read()

    window.close()

    if event == 'Yes':
        customer_page()
    else:
        customer_info()


def add_book_to_database(name, author, qty, price):
    conn = sqlite3.connect("Library.db")

    c = conn.cursor()

    c.execute("SELECT BId FROM Book;")
    var = len(c.fetchall())
    var += 1

    query = "INSERT INTO Book VALUES({id}, '{n}', '{a}', {q}, {p});"
    query = query.format(n=name, a=author, q=qty, p=price)

    c.execute(query)

    conn.commit()

    conn.close()


def add_book():
    layout = [[sg.Text('Book Name'), sg.InputText(key='-name-')],
              [sg.Text('Author of the book'), sg.InputText(key='-author-')],
              [sg.Text('Number of books'), sg.InputText(key='-qty-')],
              [sg.Text('Price'), sg.InputText(key='-price-')],
              [sg.Button('Add')]]

    window = sg.Window('Welcome', layout)
    event, values = window.read()

    if values['-price-'] > 0 and values['-qty-'] > 0:
        add_book_to_database(values['-name-'], values['-author-'], values['-qty-'], values['-price'])
    else:
        pass


def choose_next():
    layout = [[sg.Button('Add a book', key='-add-')],
              [sg.Button('Remove a book', key='-remove-')],
              [sg.Button('Modify book', key='-modify-')]]

    window = sg.Window('Welcome', layout)

    event, values = window.read()

    if event == '-add-':
        add_book()
    if event == '-remove-':
        remove_book()
    if event == '-modify-':
        modify_book()

    window.close()


""" Function Calls / the main program
    Sort of like the main program - (I'm from C++)  
"""

#creating_database()
#insert_into_books()
#insert_into_customers()
#insert_into_librarian()
#insert_into_info()
choose = first_page()

if choose == 'Librarian':
    is_librarian = librarian_page()
else:
    customer_question()

# select()
if is_librarian:
    choose_next()
