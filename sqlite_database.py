import _sqlite3

connection = _sqlite3.connect('foreign_currency.db')

c = connection.cursor()

#c.execute("""CREATE TABLE foreign_currencies (
#            selection text
#            )""")

#c.execute("INSERT INTO foreign_currencies VALUES ('Australia')")

#c.execute("SELECT * FROM foreign_currencies WHERE selection='Australia'")

c.execute("INSERT INTO foreign_currencies VALUES ('India')")

c.execute("SELECT * FROM foreign_currencies WHERE selection='India'")

c.execute("SELECTG * FROM foreign_currencies WHEERE selection='Australia'")

connection.commit()

print(c.fetchall())

connection.commit()

connection.close()
