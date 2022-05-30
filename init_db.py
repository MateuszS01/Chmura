import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (nick, tytul, text) VALUES (?, ?, ?)",
            ('-Anna', 'Pierwszy Post', 'Fajna Strona!')
            )

cur.execute("INSERT INTO posts (nick, tytul, text) VALUES (?, ?, ?)",
            ('-Adam', 'Drugi Post', 'wcale nie taka fajna..')
            )

connection.commit()
connection.close()
