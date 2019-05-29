from flask import Flask, render_template, request
import psycopg2
import sys
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
con = None



@app.route("/")
def main():






        try: 
            con = psycopg2.connect("host = 'localhost' dbname = 'testdb' user = 'adialachar' password = 'squirtle123'")
            cur = con.cursor()

            #cur.execute(SQL statement)



            con.commit()

        except psycopg2.DatabaseError, e:
            if con:
                con.rollback()
            print("Error")
            sys.exit(1)



        finally:
            if con:
                con.close()


	return render_template("index.html")



if __name__ == "__main__":
	app.run()
