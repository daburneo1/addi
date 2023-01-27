import pymysql

# connection = pymysql.connect(
#     host="localhost",
#     user="root",
#     password="",
#     db="addi"
# )
connection = pymysql.connect(
    host="localhost",
    user="addi2023",
    password="addi2023",
    db="addi"
)

cursor = connection.cursor()