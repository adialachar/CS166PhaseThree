
import psycopg2
import sys


con = None


def checkPilot(pilot_name,pilot_nationality):
    
    try:
        con = psycopg2.connect("host = 'localhost' dbname = 'testdb' user = 'adialachar' password = 'squirtle123'")
        cur = con.cursor()



        cur.execute("SELECT * FROM Pilot P WHERE P.fullname = '{}';".format(pilot_name))

        while True:
            row = cur.fetchone()

            if row == None:

                cur.execute("INSERT INTO Pilot (id,fullname,nationality) VALUES(nextval('PilotID'), '{}', '{}');".format(pilot_name, pilot_nationality))
                con.commit()
                return None



                

            else:

                return row[0]


    except psycopg2.DatabaseError as e:
            if con:
                con.rollback()
            print("Error")
            print(e)
            sys.exit(1)



    finally:
        if con:
            con.close()











    




def checkPlane(make,model,age,seats):




    try:
        con = psycopg2.connect("host = 'localhost' dbname = 'testdb' user = 'adialachar' password = 'squirtle123'")
        cur = con.cursor()



        cur.execute("SELECT * FROM Plane P WHERE P.make = '{}' AND P.model = '{}' AND P.age = '{}' AND P.seats = '{}' ;".format(make,model,age,seats))

        while True:
            row = cur.fetchone()

            if row == None:

                cur.execute("INSERT INTO Plane(id,make,model,age,seats) VALUES (nextval('PlaneID'), '{}', '{}', '{}', '{}');".format(make,model,age,seats))
                con.commit()

                return None



            else:
                return row[0]


    except psycopg2.DatabaseError as e:
        if con:
            con.rollback()
            print("Error")
            print(e)
            sys.exit(1)


    finally:
        if con:
            con.close()

    

    
    
def checkCustomer(fname,lname,gender,dob,address,phone,zipcode):



    try:
        con = psycopg2.connect("host = 'localhost' dbname = 'testdb' user = 'adialachar' password = 'squirtle123'")
        cur = con.cursor()



        cur.execute("SELECT * FROM Customer C WHERE C.fname = '{}' AND C.lname = '{}' AND C.dob = '{}' ;".format(fname,lname,dob))

        while True:
            row = cur.fetchone()

            if row == None:

                cur.execute("INSERT INTO Customer (id,fname,lname,model,age,seats) VALUES (nextval('CustomerID'), '{}', '{}', '{}', '{}','{}','{}','{}');".format(fname,lname,gender,dob,address,phone,zipcode))
                con.commit()

                return None





            else:
                return row[0]


    except psycopg2.DatabaseError as e:
        if con:
            con.rollback()
        print("Error")
        print(e)
        sys.exit(1)

    finally:
        if con:
            con.close()
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
