import sqlite3


def connect():
    conn= sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isdn integer )")
    conn.commit()
    conn.close()

def insert(title, author, year, isdn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isdn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year="", isdn=""):
    conn = sqlite3.connect("books.db")
    cur =  conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isdn=?",(title, author, year, isdn))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn =  sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id,title,author,year,isdn):
    conn =  sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isdn=? WHERE id=? ",(title, author, year, isdn,id))
    conn.commit()
    conn.close()

connect()
#insert("Seagull", "anton chekhov", 1912, 5797825563)
#update(2, "The Seagull","Anton Chekhov", 1896, 4583551321)
#delete(1)
print(view())
