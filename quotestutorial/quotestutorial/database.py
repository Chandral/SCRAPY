import sqlite3
conn = sqlite3.connect('myquotes.db')
c = conn.cursor()
c.execute("CREATE TABLE quotes_tb (title text, author text, tags text)")
conn.commit()
conn.close()