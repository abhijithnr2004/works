from mysql import connector

class Vehicles :

    def __init__(self):
        
        try :

            self.connection = connector.connect(

                host = "localhost",
                user = "root",
                password = "Password@123",
                db = "gosell_db"
            )

            self.cursor = self.connection.cursor()

            print("DB connected...")

        except Exception as e :

            print(e)

    def add_vehicle(self,**kwargs) :

        try :

            columns = ""
            values = ""

            for k,v in kwargs.items():

                columns += k+","
                values+="%s"+","

            columns = columns.rstrip(",")
            values = values.rstrip(",")

            query = f"""
                insert into vehicle ({columns}) values ({values})

            """

            data = tuple(v for v in kwargs.values())

            self.cursor.execute(query,data)

            self.connection.commit()

            print("Data inserted")

        except Exception as e :

            print(e)

    def list_vehicles(self) :

        try :

            query = """
                select * from vehicle

            """

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for row in records :

                print(row)
            
        except Exception as e:

            print(e)

    def retrieve_vehicles(self,id) :

        try :

            query = f"""
                select * from vehicle where id = {id}

            """

            self.cursor.execute(query)

            records = self.cursor.fetchone()

            print(records)
            
        except Exception as e:

            print(e)

    def delete_vehicles(self,id=None) :

        try :

            query = """
                delete from vehicle where id = %s

            """

            self.cursor.execute(query,(id,))

            self.connection.commit()

            print("record deleted....")
            
        except Exception as e:

            print(e)
        
    def update_vehicles(self,id,**kwargs):

        place_holder = ""

        try :
            
            for k,v in kwargs.items():

                place_holder += k + "=" + "%s" + ","

            place_holder = place_holder.rstrip(",")

            query = f"update vehicle set {place_holder} where id = {id}"
            
            data = [v for k,v in kwargs.items()]

            self.cursor.execute(query,data)

            self.connection.commit()

            print("record updated....")
        
        except Exception as e:

            print(e)
    
vehicle_instance = Vehicles()


# vehicle_instance.add_vehicle(name="passion pro",price=30000,year=2015,fuel_type = "petrol",comments="showroom condition",running_km=10000,
#                              owner_type="single",owner="vijay",location="thrissur")

vehicle_instance.list_vehicles()

# vehicle_instance.retrieve_vehicles(2)

# vehicle_instance.delete_vehicles(3)

# vehicle_instance.update_vehicles(column_name="year",value="2018",id=2)
