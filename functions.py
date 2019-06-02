
import psycopg2
import sys


con = None


def checkPilot(pilot_name,pilotstuff):
    
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











    




def checkPlane():

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

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    return 0
