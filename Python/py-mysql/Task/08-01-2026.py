from mysql import connector


class Hospital :


    def __init__(self) :

        try :

            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="Password@123",
                db="hospital_db"
            )

            self.cursor = self.connection.cursor()

            print("Database connected...")

        except Exception as e :

            print(e)


    
    def add_patient(self, **kwargs) :

        try :

            columns = ""
            values = ""

            for k,v in kwargs.items() :

                columns += k + ","
                values += "%s,"

            columns = columns.rstrip(",")
            values = values.rstrip(",")

            query = f"insert into patients ({columns}) values ({values})"

            data = tuple(v for v in kwargs.values())

            self.cursor.execute(query, data)

            self.connection.commit()

            print("Patient added...")

        except Exception as e :

            print(e)


   
    def list_patients(self) :

        try :

            query = "select * from patients"

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for row in records :

                print(row)

        except Exception as e :

            print(e)


   
    def retrieve_patient(self, id) :

        try :

            query = "select * from patients where id = %s"

            self.cursor.execute(query, (id,))

            record = self.cursor.fetchone()

            print(record)

        except Exception as e :

            print(e)


    
    def update_patient(self, id, **kwargs) :

        try :

            place_holder = ""

            for k,v in kwargs.items() :

                place_holder += k + "=%s,"

            place_holder = place_holder.rstrip(",")

            query = f"update patients set {place_holder} where id = {id}"

            data = tuple(v for v in kwargs.values())

            self.cursor.execute(query, data)

            self.connection.commit()

            print("Patient updated...")

        except Exception as e :

            print(e)


    
    def delete_patient(self, id) :

        try :

            query = "delete from patients where id = %s"

            self.cursor.execute(query, (id,))

            self.connection.commit()

            print("Patient deleted...")

        except Exception as e :

            print(e)



hospital_instance = Hospital()


# hospital_instance.add_patient(name="Ravi",age=45,gender="male",disease="Diabetes",doctor="Dr. Arun")
# hospital_instance.add_patient(name="Anita",age=32,gender="female",disease="Fever",doctor="Dr. Meena")



hospital_instance.list_patients()



# hospital_instance.retrieve_patient(1)



# hospital_instance.update_patient(3,disease="High BP",name = "Babu")


# hospital_instance.delete_patient(4)
