from flask import Flask, render_template, request
import psycopg2
import sys
import csv
import functions
#import checkPlane from functions
#import checkPilot from functions
'''
import customer    
import flights  
import planes   
import reservation  
import technician
import flightinfo  
import pilots   
import repairs  
import schedule
'''
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
con = None



@app.route("/", methods = ['GET', 'POST'])
def main():




    return render_template("index.html")
         




@app.route("/plane", methods = ['GET', 'POST'])
def Plane():


    if request.method == 'POST':
        data = request.form


            #print(data.get('id',-1))
        print(data.get('Make',-1))
        print(data.get('Model',-1))
        print(data.get('Age',-1))
        print(data.get('seats',-1))

        Make = data.get('Make',-1)
        Model = data.get('Model',-1)
        Age = data.get('Age',-1)
        Seats = data.get('seats',-1)

        Seats = int(Seats)




        try: 
            con = psycopg2.connect("host = 'localhost' dbname = 'testdb' user = 'adialachar' password = 'squirtle123'")
            cur = con.cursor()


            #cur.execute("GRANT ALL ON SCHEMA public TO postgres;")
            '''
            cur.execute("SELECT * FROM Reservation R where R.status = 'W' LIMIT 20;")

            while True:
                row = cur.fetchone()

                if row == None:
                    break

                print("rnum {0} , cid {1}, fid {2}, status {3}".format(row[0], row[1], row[2], row[3]))

            #con.commit()
            '''




            #cur.execute("INSERT INTO Flight (fnum,cost,num_sold,actual_departure_date, actual_arrival_date  rrival-airport, departure_airport)  VALUES (nextval('FlightNum'), ..................);")
            #cur.execute("INSERT INTO Plane   values(nextval('PlaneID'),...............);")
            #cur.execute("INSERT INTO Pilot (id,fullname,nationality) VALUES (nextval('PilotID'),'Aditya Acharya','indian');")
            #cur.execute("INSERT INTO Technician VALUES(nextval('TechID')")

            

            #con.commit()


            cur.execute("INSERT INTO Plane (id,make,model,age,seats) VALUES (nextval('PlaneID'), '{}', '{}' , '{}', '{}')".format(Make, Model, Age, Seats))
            con.commit()

        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print("Error")
            print(e)
            sys.exit(1)



        finally:
            if con:
                con.close()
    

    return render_template("plane.html")



@app.route("/pilot", methods = ['GET','POST'])
def Pilot():


    if request.method == 'POST':
        data = request.form

        full_name = data.get('Full Name',-1)
        nationality = data.get('Nationality',-1)



        print(full_name)
        print(nationality)

	
        try:
            con = psycopg2.connect("host = 'localhost' dbname = 'testdb' user = 'adialachar' password = 'squirtle123'")
            cur = con.cursor()
        


            cur.execute("INSERT INTO Pilot(id, fullname, nationality) VALUES (nextval('PilotID'), '{}', '{}')".format(full_name, nationality))
            con.commit()


        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print("Error")
            print(e)
            sys.exit(1)



        finally:
            if con:
                con.close()


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	



    return render_template("pilot.html")

@app.route("/technician", methods = ['GET','POST'])
def Tech():


    if request.method == 'POST':
        data = request.form

        full_name = data.get('fullname',-1)

        print(full_name)

	
	
        try:
            con = psycopg2.connect("host = 'localhost' dbname = 'testdb' user = 'adialachar' password = 'squirtle123'")
            cur = con.cursor()
        


            cur.execute("INSERT INTO Technician (id, full_name) VALUES (nextval('TechID'), '{}');".format(full_name))


            con.commit()



        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print("Error")
            print(e)
            sys.exit(1)


        finally:
            if con:
                con.close()


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

    return render_template("technician.html")


@app.route("/flight", methods = ['GET','POST'])
def Flight():



    if request.method == 'POST':
        data = request.form


        cost = data.get('Cost',-1)
        seats_sold = data.get('SeatsSold',-1)
        num_stops = data.get('numstops',-1)
        a_d_d = data.get('ADd',-1)
        a_a_d = data.get('AAd',-1)
        AA = data.get('AA',-1)
        DA = data.get('DA',-1)

        pilot_name = data.get("pilot_full_name", -1)
        pilot_nationality = data.get("pilot_nationality",-1)

        plane_make = data.get("plane_make", -1)
        plane_model = data.get("plane_model", -1)
        plane_age = data.get("plane_age", -1)
        plane_seats = data.get("plane_seats",-1)

        


        print(cost)
        print(seats_sold)
        print(num_stops)
        print(a_d_d)
        print(a_a_d)
        print(AA)
        print(DA)
        print(pilot_name)
        print(plane_make)

	
	
	
	
	
	
        try:
            con = psycopg2.connect("host = 'localhost' dbname = 'testdb' user = 'adialachar' password = 'squirtle123'")
            cur = con.cursor()
        
            #REMEMBER TO MAKE A SEQUENCE FOR FLIGHTINFO
            # Check if the pilot exists
            # Check if the Plane exists

            pilotID = functions.checkPilot(pilot_name, pilot_nationality)
            planeID = functions.checkPlane(plane_make, plane_model, plane_age, plane_seats)

            if pilotID == None:


                cur.execute("Select * from pilot P where P.fullname = '{}' and P.nationality = '{}' ;".format(pilot_name,pilot_nationality))

            
                row = cur.fetchone()

                if row == None:
                    print("There is something very wrong here. This is the programs fault, not the user's")


                pilotID = row[0]
                    






            if planeID == None:





                cur.execute("select * from plane P where P.make = '{}' and P.model = '{}' and P.age = '{}' and P.seats = '{}'".format(plane_make,plane_model,plane_age,))

                row = cur.fetchone()

                if row == None:
                    print("Thre is something very wrong here.")


                planeId = row[0]

                




            
            cur.execute("INSERT INTO Flight (fnum,cost,num_sold,num_stops,actual_departure_date, actual_arrival_date,arrival_airport, departure_airport)  VALUES (nextval('FlightNum'),'{}','{}','{}','{}','{}','{}','{}');".format(cost,seats_sold,num_stops,a_d_d, a_a_d, AA,DA))











            cur.execute("INSERT INTO FlightInfo (fiid, flight_id, pilot_id, plane_id) VALUES (nextval('FlightInfoID'), (SELECT fnum from Flight F where F.cost = '{}' and F.num_sold = '{}' and F.actual_departure_date = '{}' and F.actual_arrival_date = '{}' and arrival_airport = '{}' and departure_airport = '{}'), '{}', '{}');".format(cost,seats_sold,a_d_d, a_a_d, AA, DA, pilotID, planeID))




        













            con.commit()


        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print("Error")
            print(e)
            sys.exit(1)



        finally:
            if con:
                con.close()


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

    return render_template("flight.html")


@app.route("/bookflight", methods = ['GET','POST'])
def BookFlight():
	
    if request.method == 'POST':

        data = request.form
        flight_number = data.get("flight_number",-1)
        customer_fname = data.get("customer_fname",-1)
        customer_lname - data.get("customer_lname",-1)
        customer_gender = data.get("customer_gender",-1)
        customer_DOB = data.get("customer_DOB",-1)
        customer_address = data.get("customer_address",-1)
        customer_phone = data.get("customer_phone",-1)
        customer_zipcode = data.get("customer_zipcode",-1)



        customer_id = functions.checkCustomer(customer_fname,customer_lname,customer_gender,customer_DOB,customer_address,customer_phone,customer_zipcode)



        if customer_id == None:

            cur.execute("select id from Customer C where C.fname = '{}' and C.lname = '{}' and C.DOB = '{}';".format(customer_fname,customer_lname,customer_DOB
            customer_id = cur.fetchone()[0]


        try:
            con = psycopg2.connect("host = 'localhost' dbname = 'testdb' user = 'adialachar' password = 'squirtle123'")
            cur = con.cursor()
        


            cur.execute("select num_sold from flight where flight.fnum = '{}'".format(flight_number))
            num_sold = None
            while True:
                row = cur.fetchone()

                if row == None:
                    break
                print(row)
                print(row[0])

                print(type(row[0]))
                num_sold = row[0]
                


            cur.execute("select num_seats from Plane P, flightinfo F where F.fid = '{}' and F.plane_id = P.id;".format(flight_number)


            row = cur.fetchone()
            num_seats = row[0]
            
            if num_sold < num_seats:
                cur.execute("Insert into reservation (rnum,cid,fid,status) values (nextval('ResNum'),'{}','{}','R');".format(customer_id,flight_number)
            else:
                cur.execute("Insert into reservation (rnum,cid,fid,status) values (nextval('ResNum'),'{}','{}', 'W');".format(customer_id,flight_number)
            



        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print("Error")
            print(e)
            sys.exit(1)



        finally:
            if con:
                con.close()


	
	
	
	
	
	
	
	
	
	
	
	
	
    return render_template("bookflights.html")

@app.route("/available_seats", methods = ['GET', 'POST'])
def AvailableSeats():
	
    if request.method == 'POST':
        try:
            con = psycopg2.connect("host = 'localhost' dbname = 'testdb' user = 'adialachar' password = 'squirtle123'")
            cur = con.cursor()
        


            cur.execute("SELECT DISTINCT P.seats FROM FlightInfo FI, Flight F, Plane P WHERE FI.flight_id = %s AND F.actual_departure_date = %s AND P.id = FI.plane_id".format())

            while True:
                row = cur.fetchone()

                if row == None:
                    break

                print("Seats {0}".format(row[0]))




            cur.execute("SELECT num_sold FROM Flight WHERE fnum = %s"())

            while True:
                row = cur.fetchone()
                if row == None:
                    break
                print("Seats {0}".format(row[0]))



        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print("Error")
            print(e)
            sys.exit(1)



        finally:
            if con:
                con.close()


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
    return render_template("available_seats.html")

@app.route("/repairs_per_plane_desc", methods = ['GET', 'POST'])
def repairs_per_plane():





    if request.method == 'POST':

        try:
            con = psycopg2.connect("host = 'localhost' dbname = 'testdb' user = 'adialachar' password = 'squirtle123'")
            cur = con.cursor()
        


            cur.execute("SELECT COUNT(R.rid) AS mycount, P.id FROM Plane P, Repairs R WHERE R.plane_id = P.id GROUP BY P.id ORDER BY mycount desc;")

            while True:
                row = cur.fetchone()

                if row == None:
                    break

                print("PlaneID {0} , number of repairs {1}".format(row[0], row[1]))



        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print("Error")
            print(e)
            sys.exit(1)


        finally:
            if con:
                con.close()











    return render_template("repairs_per_plane.html")
@app.route("/repairs_per_year_asc", methods = ['GET', 'POST'])
def repairs_per_year():


    if request.method == 'POST':




        try:
            con = psycopg2.connect("host = 'localhost' dbname = 'testdb' user = 'adialachar' password = 'squirtle123'")
            cur = con.cursor()
        


            cur.execute("SELECT date_part('year', R1.repair_date) AS R_year, COUNT(R2.id) AS myCount FROM Repairs R1, Repairs R2 WHERE R1.id = R2.id GROUP BY R_year ORDER BY myCount ASC;")

            while True:
                row = cur.fetchone()

                if row == None:
                    break

                print("YEAR {0} , number of repairs {1}".format(row[0], row[1]))



        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print("Error")
            print(e)
            sys.exit(1)



        finally:
            if con:
                con.close()



    return render_template("repairs_per_year.html")

@app.route("/passenger_status", methods = ['GET', 'POST'])
def passenger_status():
	
	
	
	
    if request.method == 'POST':
	
	
        try:
            con = psycopg2.connect("host = 'localhost' dbname = 'testdb' user = 'adialachar' password = 'squirtle123'")
            cur = con.cursor()
        


            cur.execute("SELECT COUNT(*) FROM Reservation R WHERE R.fid = %s AND R._status = %s;"())

            while True:
                row = cur.fetchone()

                if row == None:
                    break

                print("{0}".format(row[0]))



        except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print("Error")
            print(e)
            sys.exit(1)



        finally:
            if con:
                con.close()


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
    return render_template("passenger_status.html")



if __name__ == "__main__":
	app.run()
