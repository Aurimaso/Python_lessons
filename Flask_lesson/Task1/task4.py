from flask import Flask, request, render_template
app = Flask(__name__)

def get_leap_year(x:int) -> bool:
    if x % 400 ==0 or x % 100 != 0 and x % 4 == 0:       
        return True
    return False

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        try:
            if get_leap_year(int(request.form['year'])):
                result = "This is a leap year"
            result = "This is not a leap year"
            return render_template("leap_result.html", result=result)
        except ValueError as e: 
            return render_template("leap_result.html", result="NO ANtanas here")
    return render_template("leap.html")

if __name__ == "__main__":
    app.run()