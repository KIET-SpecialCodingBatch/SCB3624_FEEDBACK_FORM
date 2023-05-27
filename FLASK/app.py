from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/")  
def home():
    return render_template("index.html")

@app.route("/form",methods=["POST","GET"])

def form():
    name=request.form.get("name","none")
    rollno=request.form.get("rollno")
    date=request.form.get("date")
    option = request.form.get('options')
    email=request.form.get("email")
    contact=request.form.get("contact")
    choice=request.form.get("choice")
    courses=request.form.get("courses")
    return render_template("form.html",name=name,rollno=rollno,date=date,option=option,email=email,contact=contact,choice=choice,courses=courses)
if __name__ =="__main__":
    app.run(debug=True)
