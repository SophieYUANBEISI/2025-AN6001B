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


@app.route("/dbs_prediction", methods=["GET", "POST"])
def dbs_prediction():
    if request.method == "GET":
        # 比如直接访问这个网址时，随便返回一点东西
        return "Please submit the form."

    q_str = request.form.get("q")
    print("q_str:", q_str)
    q = float(q_str)
    model = joblib.load("dbs.pkl")
    r = model.predict([[q]])[0]
    return render_template("dbs_prediction.html", r=r)

if __name__ == "__main__":
    app.run()
    


