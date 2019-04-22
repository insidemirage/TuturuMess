from form import Window
import configparser
import sqlite3

connection = sqlite3.connect("data.db") 
cursor = connection.cursor()
cursor.execute("""SELECT * FROM logdata""")
dates = cursor.fetchall()

def main():
    Form = Window(dates)
    Form.InitForm()
    # CreateForm(config['kwork']['pass'], config['kwork']['login'])
    #tututut21
main()