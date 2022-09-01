from flask import Flask, jsonify, render_template, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

app.config["MYSQL_DB"] = "bcxtkd0upzojf7dyt91g"
app.config["MYSQL_HOST"] = "bcxtkd0upzojf7dyt91g-mysql.services.clever-cloud.com"
app.config["MYSQL_PASSWORD"] = "cqYifZsBlo03hxsIUqod"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_URI"] = "mysql://utxs5ess1sj38hy8:cqYifZsBlo03hxsIUqod@bcxtkd0upzojf7dyt91g-mysql.services.clever-cloud.com:3306/bcxtkd0upzojf7dyt91g"
app.config["MYSQL_USER"] = "utxs5ess1sj38hy8"
app.config["MYSQL_VERSION"] = 8.0

mysql = MySQL(app)

# HOMEPAGE
@app.route("/")
def homepage():
    return render_template("index.html")


# TAKING ALL DATA
@app.route("/quiz/<category>", methods=["GET"])
def get_data(category):
    global category_data

    conn = mysql.connection
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM QUIZ WHERE category = {category}")

    all_data = cur.fetchall()
    category_data = all_data
    cur.close()
    return jsonify(all_data)


#cheking the answer
@app.route('/quiz', methods=['POST'])
def check_answer():
    global category_data
    count = 0 
    data = request.get_json()
    conn = mysql.connection
    cur = conn.cursor()

    data = data["answer"]
    for counter, user_answer in enumerate(data):
        if category_data[counter][2] == user_answer:
            count += 1
    conn.commit()
    cur.close()

    return count


if __name__ == "__main__":
    app.run(debug=True)