from app import app
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

mysql = MySQL(app)
bcrypt = Bcrypt(app)
# connect to MySQL database hosted on AWS free tier
app.config['MYSQL_USER'] = "admin"
app.config['MYSQL_PASSWORD'] = "BT2102group16"
app.config['MYSQL_DB'] = "bt2102-oshes"
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_HOST'] = "bt2102-oshes.c1j7ubdkf9mu.ap-southeast-1.rds.amazonaws.com"

mysql.init_app(app)
