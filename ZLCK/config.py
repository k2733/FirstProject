#数据库的配置变量
HOSTNAME = 'VPC2201010'
PORT = '1433'
DATEBASE = 'FlaskDatabase'
USENAME = 'sa'
PASSWORD = 'vcc2022!'

DB_URI = 'mssql+pymssql://{}:{}@{}:{}/{}' .format(USENAME,PASSWORD,HOSTNAME,PORT,DATEBASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'adlfjlasjflsaldfjladf'