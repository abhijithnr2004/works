from mysql import connector

connection = connector.connect(
    host = "localhost",
    user = "root",
    password = "Password@123",
    database = "tripwise_db"
)

cursor = connection.cursor()

query = """
    
    insert into user (name,email,password) values (%s,%s,%s)

"""

data = [("Abhijith","Abhijith@gmail.com","pass123456"),
        ("ashik","ashik@gmail.com","abc123"),
        ("vivek","vivek@gmail.com","abcdefg")
        ]

cursor.executemany(query,data)

connection.commit()

print("Query executed.....")

cursor.close()

connection.close()