from mysql import connector

connection = connector.connect(
    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "tripwise_db"
)

cursor = connection.cursor()

query = "delete from user where id = %s"

data = (2,)

cursor.execute(query,data)

connection.commit()

print("record deleted")

cursor.close()

connection.close()
