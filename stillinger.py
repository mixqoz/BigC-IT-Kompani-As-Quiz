from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_jobs():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="your_password",
        database="your_database",
        auth_plugin="mysql_native_password"
    )
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM jobs")
    return cursor.fetchall()

@app.route("/")
def index():
    jobs = get_jobs()
    return render_template("index.html", jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True)
