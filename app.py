from flask import Flask, render_template, request
import psycopg2
import sys
import csv
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




    return render_template("pilot.html")

@app.route("/technician", methods = ['GET','POST'])
def Tech():


    if request.method == 'POST':
        data = request.form

        full_name = data.get('fullname',-1)

        print(full_name)


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

        print(cost)
        print(seats_sold)
        print(num_stops)
        print(a_d_d)
        print(a_a_d)
        print(AA)
        print(DA)



    return render_template("flight.html")


@app.route("/bookflight", methods = ['GET','POST'])
def BookFlight():
    return render_template("bookflight.html")

@app.route("/available_seats", methods = ['GET', 'POST'])
def AvailableSeats():
    return render_template("available_seats.html")

@app.route("/repairs_per_plane_desc", methods = ['GET', 'POST'])
def repairs_per_plane():


    











    return render_template("repairs_per_plane.html")
@app.route("/repairs_per_year_asc", methods = ['GET', 'POST'])
def repairs_per_year():

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
    return render_template("passenger_status.html")



if __name__ == "__main__":
	app.run()
