from flask import Flask,render_template

app = Flask(__name__)
items = [
    {"id" : 1 ,"name" : "Peanut Butter" , "barcode" : "1m3j3414j" , "price" : 712},
    {"id" : 2 ,"name" : "MB Whey Protien" , "barcode" : "45j32hj2h" , "price" : 5199},
    {"id" : 3 ,"name" : "MB CreaPure" , "barcode" : "345j2kf9f" , "price" : 1599},
    {"id" : 4 ,"name" : "Fish Oil" , "barcode" : "64j4j3i2d" , "price" : 899},
]
@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route('/market')
def market_page():
    return render_template("market.html",items=items)
