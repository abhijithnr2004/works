from mysql import connector

connection = connector.connect(
    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "tripwise_db"
)

cursor = connection.cursor()

query = """
    select * from user
"""
cursor.execute(query)

records = cursor.fetchall()

for row in records:

    print(row)

cursor.close()
connection.close()