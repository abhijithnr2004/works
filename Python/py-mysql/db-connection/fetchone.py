from mysql import connector

connection = connector.connect(
    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "tripwise_db"
)

cursor = connection.cursor()

query = "select * from user where id = %s"

data = (2,)

cursor.execute(query,data)

records = cursor.fetchone()

print(records)

cursor.close()

connection.close()