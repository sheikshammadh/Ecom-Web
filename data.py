from flask import Flask, request, jsonify, render_template
import MySQLdb

app = Flask(__name__)

# Database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'login_page_db'

# Initialize MySQL
mysql = MySQLdb.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    db=app.config['MYSQL_DB']
)

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    region_code = request.form.get('region_code')
    mobile_no = request.form.get('mobile_no')
    email = request.form.get('email')

    cursor = mysql.cursor()
    cursor.execute("INSERT INTO users (first_name, last_name, region_code, mobile_no, email) VALUES (%s, %s, %s, %s, %s)", 
                   (first_name, last_name, region_code, mobile_no, email))
    mysql.commit()
    cursor.close()

    return "Data submitted successfully!"

if __name__ == "__main__":
    app.run(debug=True)