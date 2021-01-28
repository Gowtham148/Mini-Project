# Importing the necessary libraries
import sqlite3


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


def populate_customer():
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    c.execute("INSERT INTO Customer VALUES(1,'John',29,'M','New York','john10');")
    c.execute("INSERT INTO Customer VALUES(2,'Jim',36,'M','Texas','jim10');")
    connection.commit()
    connection.close()


def populate_librarian():
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    c.execute("INSERT INTO Librarian VALUES(100,'Claire',26,'F','London','claire10');")
    c.execute("INSERT INTO Librarian VALUES(101,'Ben',44,'M','Paris','ben10');")
    connection.commit()
    connection.close()


def change_librarian_password(name, age, city, password):
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    query = "UPDATE Librarian SET Password = '{p}' WHERE Name = '{n}' AND Age = {a} AND City = '{c}';"
    query = query.format(p=password, n=name, a=age, c=city)
    c.execute(query)
    connection.commit()
    connection.close()


def populate_new_customer(name, age, sex, city, password):
    connection = sqlite3.connect("Library.db")
    c = connection.cursor()
    c.execute("SELECT COUNT(*) FROM Customer;")
    variable = c.fetchall()
    query = "INSERT INTO Customer VALUES();"
    print(variable)
    connection.commit()
    connection.close()
