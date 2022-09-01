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



if __name__ == "__main__":
    app.run(debug=True)