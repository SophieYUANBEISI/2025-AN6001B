from flask import Flask,render_template,request
import joblib
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    print(q)
    return(render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    return(render_template("dbs.html"))

@app.route("/dbs_prediction",methods=["GET","POST"])
def dbs_prediction():
    q = float.form.get("q")
    print(q)
    model = joblib.load("/content/dbs.pkl")
    r = model.predict([[q]])
    return(render_template("dbs_prediction.html, r=r"))

if __name__ == "__main__":
    app.run()
    


