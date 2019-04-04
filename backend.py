import sqlite3

class Database:
    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isdn integer )")
        self.conn.commit()

    def insert(self,title, author, year, isdn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isdn))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search(self,title="", author="", year="", isdn=""):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isdn=?",(title, author, year, isdn))
        rows = self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))
        conn.commit()

    def update(self,id,title,author,year,isdn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isdn=? WHERE id=? ",(title, author, year, isdn,id))
        conn.commit()

    def __del__(self):
        self.conn.close()

#insert("Seagull", "anton chekhov", 1912, 5797825563)
#update(2, "The Seagull","Anton Chekhov", 1896, 4583551321)
#delete(1)
