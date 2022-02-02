from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
import os

# app = Flask(__name__)

TEMPLATE_DIR = os.path.abspath('C:/Users/vinun/OneDrive/Desktop/DesktopImp/BackupProject/flask/templates')
STATIC_DIR = os.path.abspath('C:/Users/vinun/OneDrive/Desktop/DesktopImp/BackupProject/flask/static')

# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route("/index", methods=['POST'])
def move_forward():
    #Moving forward code
    # forward_message = "Moving Forward..."
    return render_template("index.html")

# @app.route("/register", methods=['POST'])
# def move_forward1():
#     #Moving forward code
#     # forward_message = "Moving Forward..."
#     return render_template("register.html")

@app.route("/")
def home():
    # title1 = "YashNotchanged"
    return render_template("index.html")




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Fetch form data
        userDetails = request.form.get
        Name = userDetails('full_name')
        Gender = userDetails('radio')
        AadharNumber = userDetails('aadhar')
        Address = userDetails('address')
        PhoneNumber = userDetails('phone')
        Pincode = userDetails('pincode')
        Fever = userDetails('fever')
        LossOfSmellandTaste = userDetails('lossofsmelltaste')
        Other = userDetails('other')
        MedicalHistory = userDetails('medical')
        AppointmentDate = userDetails('appointmentdate')
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
