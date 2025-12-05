from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app=Flask(__name__)

db=mysql.connector.connect(
    host="localhost",
    username="root",
    password="",
    database="flask"
)
db.connect()
cursor=db.cursor()

@app.route('/')
def index():
    return render_template("login.html")
@app.route('/login',methods=['POST'])
def add_user():
    username=request.form.get("username")
    password=request.form.get("password")

    cursor.execute(
        "INSERT INTO login_form(username,pass_word)VALUES(%s, %s)",
         (username,password)
)
    db.commit()
    return render_template("execute.html", username= username,password= password)  

@app.route('/login', methods=['GET'])
def show_all():
    cursor.execute("SELECT * FROM login_form")
    rows = cursor.fetchall()
    return render_template('execute.html', data=rows)

if __name__ == '__main__':
    app.run(debug=True)