import cx_Oracle
import pandas as pd
# coding:utf-8

# file => dict

file_dict = {}


#增（insert）

#删（delete）

#查（select）

#改（update）

class operate_OracleDB():
    def __init__(self) :
        self.tns = cx_Oracle.makedsn("dx.huangyi.cn","1521","orcl")
        self.conn = cx_Oracle.connect("C##VCC","VCC",self.tns)

    # def connect_DB():
    #     tns = cx_Oracle.makedsn("dx.huangyi.cn","1521","orcl")
    #     conn = cx_Oracle.connect("C##VCC","VCC",tns)
    #     return tns,conn

    #!读取数据库数据
    def read_data():
        tns = cx_Oracle.makedsn("dx.huangyi.cn","1521","orcl")
        conn = cx_Oracle.connect("C##VCC","VCC",tns)
        cursor = conn.cursor()
        cursor.execute("select * from tb_user")
        file_dict = dict(cursor.fetchall())         #!查询结果转化为字典格式
        return file_dict

tns = cx_Oracle.makedsn("dx.huangyi.cn","1521","orcl")
conn = cx_Oracle.connect("C##VCC","VCC",tns)

    #插入新值
def inster_data(i,user,password):
        cursor = conn.cursor()
        sql = "insert into tb_user values('%s','%s')" %user %password
        try:
            cursor.execute(sql)
            conn.commit() 
            print("数据插入成功")
        except:
            conn.rollback() #发生错误时回滚
            print("语句执行错误")
        conn.close()

    #更新数据
def updata_data(username,password):
        cursor = conn.cursor()
        #更新密码，
        sql = "update tb_user set passward = '%s' WHERE user = '%s'" %password %username
        try:
            cursor.execute(sql)
            conn.commit() 
            print("数据更新成功")
        except:
            conn.rollback() #发生错误时回滚
            print("语句执行错误")
        conn.close()

        
if __name__ == "__main__":
    print(operate_OracleDB.read_data())
