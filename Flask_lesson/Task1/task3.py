from flask import Flask, render_template
import calendar

app = Flask(__name__)

@app.route("/keliamieji")
def Romas():
    return render_template("Romas.html", calendar = calendar)

if __name__ == "__main__":
    app.run(debug=True)