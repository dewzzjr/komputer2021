import mysql.connector

# > python -m pip install mysql-connector-python

mydb = mysql.connector.connect(
    host="localhost",
    user="aplikasi",
    password="2~f7`F&&QHzew~4B",
    database="aplikasi"
)


def insert(username, firstname, lastname, password):
    mycursor = mydb.cursor()
    sql = "INSERT INTO users(username, firstname, lastname, password) VALUES (%s, %s, %s, %s)"
    val = (username, firstname, lastname, password)

    mycursor.execute(sql, val)

    mydb.commit()

    rows = mycursor.rowcount
    print(rows, " baris berhasil ditambahkan")
    return rows

def getall():
    mycursor = mydb.cursor()
    sql = "SELECT username, firstname, lastname, password FROM users"
    mycursor.execute(sql)
    return mycursor.fetchall()
