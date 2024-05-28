from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/main",methods=["GET","POST"])
def main():
    r = request.form.get("q")
    return(render_template("bank_website.html",r=r))

if __name__ == "__main__":
    app.run()
