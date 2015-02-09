from flask import Flask, render_template, url_for, request
import prepop

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if request.form:
        if request.form['socialnetwork'] == "Twitter":
            p = prepop.prepop_twitter(request.form['content'])
        else:
            p = prepop.prepop_facebook(request.form['content'])
        return render_template("index.html",content=p)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
