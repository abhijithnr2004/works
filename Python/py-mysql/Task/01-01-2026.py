from mysql import connector

class jobs :

    def __init__(self):
        
        try:

            self.connection = connector.connect(

                host = "localhost",
                user = "root",
                password = "Password@123",
                db = "jobs_task_db"
            )

            self.cursor = self.connection.cursor()

            print("DB connected.....")

        except Exception as e :

            print(e)

    def add_jobs(self,**kwargs) :

        try :

            columns =""
            values = ""

            for k,v in kwargs.items() :

                columns += k + ","
                values += "%s" + ","

            columns = columns.rstrip(",")

            values = values.rstrip(",")

            query = f"insert into jobs ({columns}) values ({values})"

            data = tuple(v for v in kwargs.values())

            self.cursor.execute(query,data)

            self.connection.commit()

            print("Data inserted......")

        except Exception as e :

            print(e)

    def list_jobs(self) :

        try :

            query = """
                select * from jobs

            """

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for row in records :

                print(row)
            
        except Exception as e:

            print(e)
            
    def retrieve_jobs(self,id) :

        try :

            query = "select * from jobs where id = %s"

            self.cursor.execute(query,(id,))

            record = self.cursor.fetchone()

            print(record)

        except Exception as e :

            print(e)

    def delete_jobs(self,id) :

        try :

            query = "delete from jobs where id = %s"

            self.cursor.execute(query,(id,))

            self.connection.commit()

            print("data deleted......")

        except Exception as e :

            print(e)

    def update_jobs(self,id,**kwargs) :

        place_holder = ""

        try :

            for k,v in kwargs.items() :

                place_holder += k + "=" + "%s" + ","

            place_holder= place_holder.rstrip(",")

            query = f"update jobs set {place_holder} where id = {id}"

            data = tuple(v for v in kwargs.values())

            self.cursor.execute(query,data)

            self.connection.commit()

            print("Data updated....")

        except Exception as e :

            print(e)


jobs_instance = jobs()

# jobs_instance.add_jobs(company="TCS",role="Python Developer",salary=600000,job_type="full-time",location="Kochi")
# jobs_instance.add_jobs(company="Infosys",role="Data Analyst",salary=550000,job_type="full-time",location="Bangalore")
# jobs_instance.add_jobs(company="Wipro",role="Java Developer",salary=480000,job_type="full-time",location="Chennai")
# jobs_instance.add_jobs(company="Accenture",role="QA Engineer",salary=420000,job_type="part-time",location="Hyderabad")


jobs_instance.list_jobs()

# jobs_instance.retrieve_jobs(3)

# jobs_instance.delete_jobs(2)

# jobs_instance.update_jobs(job_type="part-time",salary = 20000,id=3)
