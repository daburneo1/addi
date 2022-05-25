import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="addi"
)

cursor = connection.cursor()