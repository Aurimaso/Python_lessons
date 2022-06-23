from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<Dainius>")
def word(Dainius):
    return render_template("word.html", Dainius = Dainius)

if __name__ == "__main__":
    app.run(debug=True)