
# Importing the PySimpleGUI for simple User Interface to make the application look good
# Importing the sqlite3 to maintain the database of the customers and the books

import sqlite3
import PySimpleGUI as sg

# Function that asks the user whether he/she is a customer or a librarian
# This function specifies the window that the user first sees in the application

# Write this function later
def returning_book():
    pass


# Write this function later
def after_customer_page():
    pass


# First page you look at this application/ Main page
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
    
    c.execute("INSERT INTO Book VALUES(1,'For whom the Bell tolls', 'Ernest Hemingway',10,750);")
    c.execute("INSERT INTO Book VALUES(2, 'Kurukku', 'Faustima Bama',10,400);")
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

    c.execute("INSERT INTO Customer VALUES(1,'John',21,'john10');")
    c.execute("INSERT INTO Customer VALUES(2,'Jim',16,'jim10')")

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

    c.execute("INSERT INTO Librarian VALUES(1,'Smith,'smith10');")
    c.execute("INSERT INTO Librarian VALUES(2,'Mark','mark10');")

    conn.commit()
    conn.close()


# Adding the book into the database - Called by the librarian
def add_book_to_database(name, author, qty, price):
    conn = sqlite3.connect("Library.db")

    c = conn.cursor()

    c.execute("SELECT BId FROM Book;")
    var = len(c.fetchall())
    var += 1

    query = "INSERT INTO Book VALUES({id}, '{n}', '{a}', {q}, {p});"
    query = query.format(id=var, n=name, a=author, q=qty, p=price)

    c.execute(query)

    conn.commit()

    conn.close()


# Getting the books information as the input form the librarian
def add_book():
    layout = [[sg.Text('Book Name'), sg.InputText(key='-name-')],
              [sg.Text('Author of the book'), sg.InputText(key='-author-')],
              [sg.Text('Number of books'), sg.InputText(key='-qty-')],
              [sg.Text('Price'), sg.InputText(key='-price-')],
              [sg.Button('Add')]]

    window = sg.Window('Welcome', layout)
    event, values = window.read()

    add_book_to_database(values['-name-'], values['-author-'], values['-qty-'], values['-price-'])

    window.close()


# Checking if the book exists in the database
def check_if_book_exists(name):
    conn = sqlite3.connect("Library.db")

    c = conn.cursor()
    c.execute("SELECT BName, Qty FROM Book;")

    answer = c.fetchall()
    conn.commit()
    conn.close()
    for i, j in answer:
        if i == name:
            return True

    return False


# Checking if number of books entered by the librarian is available
def number_of_book(name, number):
    number = int(number)
    conn = sqlite3.connect("Library.db")

    c = conn.cursor()
    c.execute("SELECT BName, Qty FROM Book;")

    temporary = c.fetchall()

    conn.commit()
    conn.close()

    for i, j in temporary:
        if i == name:
            if number <= int(j):
                return True

    return False


def delete_book_from_database(name, number):
    number = int(number)
    conn = sqlite3.connect("Library.db")
    c = conn.cursor()

    c.execute("SELECT BName, Qty FROM Book;")

    temporary = c.fetchall()
    conn.commit()
    conn.close()

    for i, j in temporary:
        if i == name:
            if int(j) == number:
                conn = sqlite3.connect("Library.db")
                c = conn.cursor()
                # query = "DELETE FROM Book WHERE BName = " + name + ";"
                query = "DELETE FROM Book WHERE BName = '{n}';"
                query = query.format(n=name)
                c.execute(query)
                conn.commit()
                conn.close()
                sg.Popup('Record deleted from the database')
                break
            else:
                new_number = int(j) - number
                conn = sqlite3.connect("Library.db")
                c = conn.cursor()
                # querys = "UPDATE Book SET Qty = " + str(new_number) + " WHERE BName = " + name + ";"
                queries = "UPDATE Book SET Qty = {num} WHERE BName = '{n}';"
                queries = queries.format(num=new_number, n=name)
                c.execute(queries)
                conn.commit()
                conn.close()
                sg.Popup('Record altered')
                break


def remove_book():
    layout = [[sg.Text('Name of the book you want to remove from the shelf'), sg.InputText(key='-name-')],
              [sg.Text('Number of books you want to take from the shelf'), sg.Input(key='-number-')],
              [sg.Button('Delete')]]

    window = sg.Window('Welcome', layout)
    event, values = window.read()

    if event == 'Delete':
        if check_if_book_exists(values['-name-']):
            if number_of_book(values['-name-'], values['-number-']):
                delete_book_from_database(values['-name-'], values['-number-'])
            else:
                sg.Popup('Reduce the number of books')
                window.close()
                remove_book()
        else:
            sg.Popup('Book you entered does not exist in the shelf')
            window.close()
            remove_book()

    window.close()


def check_book_name_to_modify(name):
    conn = sqlite3.connect("Library.db")
    c = conn.cursor()
    c.execute("SELECT BName, Qty FROM Book;")

    temporary = c.fetchall()
    conn.commit()
    conn.close()

    for i, j in temporary:
        if i == name:
            return True

    return False


def modify_book_in_database(name):
    layout = [[sg.Text('Name'), sg.InputText(key='-name-')],
              [sg.Text('Author'), sg.InputText(key='-author-')],
              [sg.Text('Qty'), sg.Input(key='-qty-')],
              [sg.Text('Price'), sg.Input(key='-price-')],
              [sg.Button('Modify')]]

    window = sg.Window('Modify what you want to change', layout)

    event, values = window.read()
    values['-qty-'] = int(values['-qty-'])
    values['-price-'] = float(values['-price-'])

    conn = sqlite3.connect("Library.db")
    c = conn.cursor()
    query = "UPDATE BOOK SET BName = '{n}', Author = '{a}', Qty = {q}, Price = {p} WHERE BName = '{na}';"
    query = query.format(n=values['-name-'], a=values['-author-'], q=values['-qty-'], p=values['-price-'], na=name)

    c.execute(query)
    conn.commit()
    conn.close()

    window.close()


def modify_book():
    layout = [[sg.Text('Book you want to modify? '), sg.InputText(key='-name-')],
              [sg.Button('Modify')]]

    window = sg.Window('Modify Book', layout)
    event, values = window.read()
    if check_book_name_to_modify(values['-name-']):
        modify_book_in_database(values['-name-'])
    else:
        sg.Popup('No record found')

    window.close()


def check_if_existing(name, password):
    conn = sqlite3.connect("Library.db")
    c = conn.cursor()
    c.execute("SELECT Name, Password from Customer;")

    variable = c.fetchall()

    conn.commit()
    conn.close()

    for i, j in variable:
        if i == name and j == password:
            return True

    return False


def get_input():
    layout = [[sg.Text('Customer Name'), sg.Input(key='-name-')],
              [sg.Text('Password'), sg.Input(key='-pass-')],
              [sg.Button('Check')]]

    window = sg.Window('Checking Customer', layout)
    event, values = window.read()

    window.close()

    if check_if_existing(values['-name-'], values['-pass-']):
        return True

    return False


def check_quantity(quantity):
    conn = sqlite3.connect("Library.db")
    c = conn.cursor()
    c.execute("SELECT Quantity, BName FROM Book;")
    variable = c.fetchall()

    conn.commit()
    conn.close()

    for i, j in variable:
        if i >= quantity:
            return  True

    return False


def lending_book_details():
    layout = [[sg.Text('Name of the book'), sg.Input(key='-name-')],
              [sg.Text('Author'), sg.Input(key='-author-')],
              [sg.Text('Quantity'), sg.Input(key='-qty-')],
              [sg.Button('Lend Book')]]

    window = sg.Window('Lend Book', layout)
    event, values = window.read()

    if check_book_name_to_modify(values['-name-']):
        if check_quantity(values['-qty-']):
            pass
        else:
            sg.Popup('Not enough books')
    else:
        sg.Popup('Book does not exist')


def lend_book():
    layout = [[sg.Text('Existing Customer')],
              [sg.Button('Yes'), sg.Button('No')]]

    window = sg.Window('Customer Verification', layout)

    event, values = window.read()

    if event == 'Yes':
        if get_input():
            window.close()
            lending_book_details()
        else:
            window.close()
            sg.Popup('Customer not in the database')

    else:
        window.close()
        customer_info()


def after_librarian():
    layout = [[sg.Button('Add a new book to the shelf')],
              [sg.Button('Remove a book from the shelf')],
              [sg.Button('Modify book details')],
              [sg.Button('Lend a book')],
              [sg.Button('Book return')]]

    window = sg.Window('Welcome', layout)
    event, values = window.read()

    if event == 'Add a new book to the shelf':
        window.close()
        add_book()
    elif event == 'Remove a book from the shelf':
        window.close()
        remove_book()
    elif event == 'Modify book details':
        window.close()
        modify_book()
    elif event == 'Lend a book':
        window.close()
        lend_book()
    else:
        window.close()
        returning_book()


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
              [sg.Text('Name'), sg.InputText(key='-name-')],
              [sg.Text('Password'), sg.InputText(key='-pass-', password_char='*')],
              [sg.Button('Sign In')]]

    window = sg.Window('Librarian Details', layout)

    event, values = window.read()

    if check(values['-name-'], values['-pass-']):
        window.close()
        after_librarian()

    else:
        sg.popup('No such librarian found')
        window.close()


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


# Shows the customer page
def customer_page():
    layout = [[sg.Text('Welcome')],
              [sg.Text('Username: '), sg.InputText(key='-name-')],
              [sg.Text('Password: '), sg.InputText(key='-password-', password_char='*')],
              [sg.Button('Sign In')]]

    window = sg.Window('Customer Details', layout)

    event, values = window.read()

    if check_info(values['-name-'], values['-password-']):
        window.close()
        after_customer_page()
    else:
        window.close()
        sg.Popup('No such customer found')
        layout1 = [[sg.Button('Retry')],
                   [sg.Button('Exit')]]

        window1 = sg.Window('Oops', layout1)

        event1, values1 = window1.read()

        if event1 == 'Retry':
            window1.close()
            customer_page()
        else:
            window1.close()

"""
def select():
    conn = sqlite3.connect("Library.db")

    c = conn.cursor()

    c.execute("SELECT Name FROM Customer;")

    var = c.fetchone()

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

    c.execute(query)

    conn.commit()

    conn.close()

    sg.popup('New Customer added to the database')


# New Customer Information
def customer_info():
    layout = [[sg.Text('Name '), sg.InputText(key='-name-')],
                [sg.Text('Age '), sg.InputText(key='-age-')],
                [sg.Text('Type your password '), sg.InputText(key='-pass-', password_char='*')],
                [sg.Text('Confirm your password '), sg.InputText(key='-pass1-', password_char='*')],
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


"""
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
"""

""" Function Calls / 
    The main program      
"""

creating_database()
insert_into_books()
insert_into_customers()
insert_into_librarian()
insert_into_info()
choose = first_page()

if choose == 'Librarian':
    librarian_page()
else:
    customer_question()

# select()
# choose_next()
