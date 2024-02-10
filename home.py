from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/burger")
def burger():
    return render_template("food.html", first_food="special burger...........30 birr", second_food="normal burger.........25 birr", third_food="cheese burger.............25", fourth_food="chicken burger...........2", image="bur")
@app.route("/hot_drinks")
def hot_drinks():
    return render_template("food.html", first_food="tea...........3", second_food="coffee...........3", third_food="mankiato................4", fourth_food="milk..............3", image="hot")
@app.route("/juice")
def juice():
    return render_template("food.html", first_food="spris juice..............7", second_food="mango juice...............6", third_food="strawbery juice...............10", fourth_food="avocado juice..............8", image="jui")
@app.route("/order")
def order():
    return render_template("order.html")
  
@app.route("/pizza")
def pizza():
    return render_template("food.html", first_food="special pizza..............3", second_food="normal pizza...............25", third_food="cheese pizza...............2", fourth_food="chicken pizza..............2", image="piz_1")
@app.route("/soft_drinks")
def soft_drinks():
    return render_template("food.html", first_food="coca_cola...........3", second_food="sprite...........3", third_food="fanta................3", fourth_food="mirinda..............3", image="soft")
@app.route("/water")
def water():
    return render_template("food.html", first_food="1/4litre...........2", second_food="1/2...........3", third_food="1 litre................4", fourth_food="2 litre..............45", image="water")
@app.route("/cake")
def cake():
    return render_template("food.html", first_food="black forest...........9", second_food="white forest...........9", third_food="caramel................5", fourth_food="millifoli..............6", image="cake")
if __name__ == "__main__":
    app.run()