from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/burger")
def burger():
    return render_template("food.html", first_food="special burger...........300 birr", second_food="normal burger.........250 birr", third_food="cheese burger.............200", fourth_food="chicken burger...........200", image="bur")
@app.route("/hot_drinks")
def hot_drinks():
    return render_template("food.html", first_food="tea...........30", second_food="coffee...........30", third_food="mankiato................40", fourth_food="milk..............30", image="hot")
@app.route("/juice")
def juice():
    return render_template("food.html", first_food="spris juice..............150", second_food="mango juice...............150", third_food="strawbery juice...............100", fourth_food="avocado juice..............100", image="jui")
@app.route("/order")
def order():
    return render_template("order.html")
  
@app.route("/pizza")
def pizza():
    return render_template("food.html", first_food="special pizza..............300", second_food="normal pizza...............250", third_food="cheese pizza...............200", fourth_food="chicken pizza..............200", image="piz_1")
@app.route("/soft_drinks")
def soft_drinks():
    return render_template("food.html", first_food="coca_cola...........30", second_food="sprite...........30", third_food="fanta................30", fourth_food="mirinda..............30", image="soft")
@app.route("/water")
def water():
    return render_template("food.html", first_food="1/4litre...........20", second_food="1/2...........30", third_food="1 litre................40", fourth_food="2 litre..............45", image="water")
@app.route("/cake")
def cake():
    return render_template("food.html", first_food="black forest...........90", second_food="white forest...........90", third_food="caramel................50", fourth_food="millifoli..............60", image="cake")
if __name__ == "__main__":
    app.run()