from flask import Flask,render_template,url_for
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<my_name>')
def greetings(my_name):
    return "Welcome, " + my_name +"!"

@app.route('/square/<int:number>')
def square_num(number):
    sqrt = number * number
    return "Sqaure of " + str(number) +" is "+ str(sqrt)

if __name__ == "__main__":
    app.run(debug = True)
