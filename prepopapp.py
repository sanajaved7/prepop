from flask import Flask, render_template, url_for
import prepop

app = Flask(__name__)

@app.route("/")
def index():
    content = "This is my very first tweet of my life #wow"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
