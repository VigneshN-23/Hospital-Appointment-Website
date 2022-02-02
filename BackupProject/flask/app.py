from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route("/")
def home():
    # title1 = "YashNotchanged"
    return render_template("register.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form
        Name = userDetails['full_name']
        Gender = userDetails['radio']
        AadharNumber = userDetails['aadhar']
        Address = userDetails['address']
        PhoneNumber = userDetails['phone']
        Pincode = userDetails['pincode']
        Fever = userDetails['fever']
        LossOfSmellandTaste = userDetails['lossofsmelltaste']
        Other = userDetails['other']
        MedicalHistory = userDetails['medical']
        AppointmentDate = userDetails['appointmentdate']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(Name, Gender, AadharNumber, Address, PhoneNumber, Pincode, Fever, LossOfSmellandTaste, Other, MedicalHistory, AppointmentDate) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(Name, Gender, AadharNumber, Address, PhoneNumber, Pincode, Fever, LossOfSmellandTaste, Other, MedicalHistory, AppointmentDate))
        mysql.connection.commit()
        cur.close()
        return redirect('/user')

    return render_template('register.html')

@app.route('/user')
def user():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('user.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True)
