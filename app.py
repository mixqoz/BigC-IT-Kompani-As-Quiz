from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def get_jobs():
    db = mysql.connector.connect(
        host="db",
        user="bigcuser",
        password="bigcpass",
        database="bigc",
        port=3306,
        charset="utf8mb4"
    )


    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT id, title, location, description FROM jobs")
    jobs = cursor.fetchall()
    cursor.close()
    db.close()
    return jobs

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/recruitment')
def recruitment():
    jobs = get_jobs()
    return render_template('recruitment.html', jobs=jobs)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=1040, debug=True)
