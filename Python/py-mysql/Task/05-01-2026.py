from mysql import connector

class Expenses:

    def __init__(self):

        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="Password@123",
                db="expense_tracker_task_db"
            )

            self.cursor = self.connection.cursor()
            
            print("DB connected.....")

        except Exception as e:
            print(e)

    def add_expense(self, **kwargs):

        try:
            columns = ""
            values = ""

            for k, v in kwargs.items():
                columns += k + ","
                values += "%s,"

            columns = columns.rstrip(",")
            values = values.rstrip(",")

            query = f"insert into expenses ({columns}) values ({values})"
            data = tuple(v for v in kwargs.values())

            self.cursor.execute(query, data)
            self.connection.commit()

            print("Expense added......")

        except Exception as e:
            print(e)

    def list_expenses(self):

        try:
            query = "select * from expenses"
            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for row in records:
                print(row)

        except Exception as e:
            print(e)

    def retrieve_expense(self, id):

        try:
            query = "select * from expenses where id = %s"
            self.cursor.execute(query, (id,))

            record = self.cursor.fetchone()
            print(record)

        except Exception as e:
            print(e)


    def delete_expense(self, id):

        try:
            query = "delete from expenses where id = %s"
            self.cursor.execute(query, (id,))
            self.connection.commit()

            print("Expense deleted......")

        except Exception as e:
            print(e)


    def update_expense(self, id, **kwargs):

        try:
            place_holder = ""

            for k, v in kwargs.items():
                place_holder += k + "=%s,"

            place_holder = place_holder.rstrip(",")

            query = f"update expenses set {place_holder} where id = {id}"
            data = tuple(v for v in kwargs.values())

            self.cursor.execute(query, data)
            self.connection.commit()

            print("Expense updated......")

        except Exception as e:
            print(e)


expense_instance = Expenses()


# expense_instance.add_expense(title="Lunch",amount=250,category="food",payment_mode="cash")
# expense_instance.add_expense(title="Bus Ticket",amount=120,category="travel",payment_mode="upi")

expense_instance.list_expenses()

# expense_instance.retrieve_expense(2)

# expense_instance.update_expense(1,amount=300,payment_mode="card")

# expense_instance.delete_expense(2)
