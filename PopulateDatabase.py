# Importing the necessary libraries
import sqlite3
import random


# Function to populate the books table with pre existing values if any
def populate_books():
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
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
    connection.commit()
    connection.close()


# Function to populate the customer table with pre existing values if any
def populate_customer():
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    c.execute("INSERT INTO Customer VALUES(1,'John',21,'M','NY','John10');")
    c.execute("INSERT INTO Customer VALUES(2,'Jay',16,'F','Florida','Jay10');")
    connection.commit()
    connection.close()


# Function to populate the librarian table with pre existing values if any
def populate_librarian():
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    c.execute("INSERT INTO Librarian VALUES(100,'Jess',56,'M','NY','jess10');")
    c.execute("INSERT INTO Librarian VALUES(101,'Jim',44,'F','Chennai','jim10');")
    connection.commit()
    connection.close()


# Function to change the librarian password - Invoked from the librarian sign in page
def change_librarian_password(name, age, city, password):
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    query = "UPDATE Librarian SET Password = '{p}' WHERE Name = '{n}' AND Age = {a} AND City = '{c}';"
    query = query.format(p=password, n=name, a=age, c=city)
    c.execute(query)
    connection.commit()
    connection.close()


# Function to add a new customer to the database
def populate_new_customer(name, age, sex, city, password):
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    # c.execute("SELECT COUNT(CId), Name FROM Customer;")
    # variable = c.fetchall()
    # variable = variable[0][0] + 1
    query = "INSERT INTO Customer VALUES({id}, '{n}', {a}, '{s}', '{c}', '{p}');"
    query = query.format(id=random.randint(1, 30) + random.randint(1, 30), n=name, a=age, s=sex, c=city, p=password)
    c.execute(query)
    connection.commit()
    connection.close()


# Function to add a new book to the database
def populate_new_book(name, author, qty, price):
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    # c.execute("SELECT COUNT(BId), BName FROM Book;")
    # variable = c.fetchall()
    # variable = variable[0][0] + 1
    query = "INSERT INTO Book VALUES({id}, '{n}', '{a}', {q}, {p});"
    query = query.format(id=random.randint(1, 30) + random.randint(1, 30), n=name, a=author, q=qty, p=price)
    c.execute(query)
    connection.commit()
    connection.close()


# Function to delete a book entirely from the database
def delete_from_book(name):
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    query = "DELETE FROM Book WHERE BName = '{n}';"
    query = query.format(n=name)
    c.execute(query)
    connection.commit()
    connection.close()


# Function to lend book to a customer
def lend_book(name, author, qty):
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    query = "SELECT BName, Qty FROM Book WHERE BName = '{n}' AND Author = '{a}';"
    query = query.format(n=name, a=author)
    c.execute(query)
    variable = c.fetchall()
    variable = variable[0][1]
    final_qty = variable - qty
    query1 = "UPDATE Book SET Qty = {q} WHERE BName = '{n}' AND Author = '{a}';"
    query1 = query1.format(q=final_qty, n=name, a=author)
    c.execute(query1)
    connection.commit()
    connection.close()


# Modifying book details
def modify_book(name, author, qty, price, ename, eauthor):
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    query = """UPDATE Book SET BName = '{n}', Author = '{a}',
            Qty = {q}, Price = {p} WHERE BName = '{bn}' AND Author = '{ba}';"""
    query = query.format(n=name, a=author, q=qty, p=price, bn=ename, ba=eauthor)
    c.execute(query)
    connection.commit()
    connection.close()
