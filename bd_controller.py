import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE logdata
                   (exchange text, login text, password text)
                """)
while True:
    login = input('login: ')
    password = input('password: ')
    exchan = input('exchange: ')
    sql = "INSERT INTO logdata VALUES ('{0}', '{1}', '{2}')".format(exchan, login, password)
    cursor.execute(sql)               
    conn.commit()
    cursor.execute("""SELECT * FROM logdata""")
    print(cursor.fetchall())
    i = input("Enter text (or Enter to quit): ")
    if not i:
        break
