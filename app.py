from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/bank_website",methods=["GET","POST"])
def bank_website():
    r = request.form.get("q")
    return(render_template("bank_website.html",r=r))

if __name__ == "__bank_website__":
    app.run()
