from app import app
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt
from pymongo import MongoClient

mysql = MySQL(app)
bcrypt = Bcrypt(app)
cluster = MongoClient('mongodb://localhost:27017')
mongo = cluster['admin']
# connect to MySQL database hosted on AWS free tier
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'OSHES'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_HOST'] = '127.0.0.1'
