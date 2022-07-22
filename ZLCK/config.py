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


#邮箱配置
#本项目中使用的是qq邮箱
MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "1319261445@qq.com"
MAIL_PASSWORD = "knaxkogedmqsffai"  #smpt授权码
MAIL_DEFAULT_SENDER = "1319261445@qq.com"
