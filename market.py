from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)
class Item(db.model):
    name = db.Column(db.String(length = 30),nullable=False,unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.string(length=12),nullable=False,unique=True)
    description = db.Column(db.Strinfo)
items = [
    {"id" : 1 ,"name" : "Peanut Butter" , "barcode" : "1m3j3414j" , "price" : 712},
    {"id" : 2 ,"name" : "MB Whey Protien" , "barcode" : "45j32hj2h" , "price" : 5199},
    {"id" : 3 ,"n ame" : "MB CreaPure" , "barcode" : "345j2kf9f" , "price" : 1599},
    {"id" : 4 ,"name" : "Fish Oil" , "barcode" : "64j4j3i2d" , "price" : 899},
]
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route('/market')
def market_page():
    return render_template("market.html",items=items)

if __name__ == '__main__':  
  app.run(debug = True)
