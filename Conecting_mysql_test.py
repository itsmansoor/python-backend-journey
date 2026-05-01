import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="mydb"
)

cursor = db.cursor()

cursor.execute("SELECT * FROM students")

data = cursor.fetchall()
print(data)

insert = cursor.execute("INSERT INTO students (name, college) VALUES ('Rasool','AUP')")
db.commit()
print(insert)