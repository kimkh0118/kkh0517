import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="mysql-3a77b6b6-kkh0516.c.aivencloud.com",
    port=24630,
    user="avnadmin",
    password=os.environ.get('DB_PASSWORD'),
    database="defaultdb"
)

cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS test_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numbers INT NOT NULL
)
""")
db.commit()

@app.route('/su/jin', methods=['POST'])
def restart():
    data = request.get_json()
    input_value = data.get('inputNumber')
    sql = "INSERT INTO numbers (value) values(%s)"
    cursor.execute(sql, [input_value,])
    db.commit()

    return jsonify({"status": "success" , "message": f"{input_value}저장 완료!"})

@app.route('/', methods=['GET'])
def home():
    return render_template('kkh_0516.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=False)
