from mysql import connector

connection = connector.connect(
    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "tripwise_db"
)

cursor = connection.cursor()

query = "update user set name=%s,password=%s where id = %s"

data = ("updated","updated_password1234",1)

cursor.execute(query,data)

connection.commit()

print("record updated")

cursor.close()

connection.close()
