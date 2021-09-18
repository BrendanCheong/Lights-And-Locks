import yaml
from app import app
from flask_mysqldb import MySQL
from flask_bcrypt import Bcrypt

db = yaml.load(open('db_secrets.yaml'), Loader=yaml.FullLoader)
mysql = MySQL(app)
bcrypt = Bcrypt(app)
# connect to MySQL database hosted on AWS free tier
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_HOST'] = db['mysql_host']

mysql.init_app(app)
