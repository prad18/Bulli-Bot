import sqlite3 
con=sqlite3.connect("genshin.db")
cur=con.cursor()
con.execute("select*from gen")
data=cur.fetchall()
print(data)