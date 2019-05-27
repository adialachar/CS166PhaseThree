from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)



@app.route("/")
def main():
	return render_template("index.html")



if __name__ == "__main__":
	app.run()
