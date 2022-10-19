import sqlite3
con=sqlite3.connect('meu_banco.db')
cur=con.cursor()
cur.execute("CREATE TABLE teste(Nome text)")
con.commit()