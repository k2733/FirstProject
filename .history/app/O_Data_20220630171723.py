from unicodedata import name
import cx_Oracle
import pandas as pd
# coding:utf-8

# file => dict

file_dict = {}


#增（insert）

#删（delete）

#查（select）

#改（update）

class ConnO():
    tns = cx_Oracle.makedsn("dx.huangyi.cn","1521","orcl")  #监听Oracle数据库
    # 建立和数据库系统的连接
    conn = cx_Oracle.connect("C##VCC","VCC",tns)   #连接数据库

    #查询数据
    def read_data():
        cursor = ConnO.conn.cursor()
        cursor.execute("select * from tb_user")
        #读取整个表格
        one = cursor.fetchall()
        file1 = pd.DataFrame(one)
        file1.columns = ['ID','user','password']
        return print(file1)

    #插入新值
    def inster_data():
        cursor = ConnO.conn.cursor()


        user = 1
        password =2
        sql = "insert into tb_user values(,'%s','%s')" %user %password

        cursor.execute("insert into tb_user values(1,'admin','password')")

    #更新数据
    def updata_data():
        cursor = ConnO.conn.cursor()

        sql = "update TEST123 set XXSCORE =  XXSCORE+100 WHERE XXNAME = '%s'"%('马云')
        try:
            cursor.execute(sql)
            ConnO.conn.commit() 
            print("数据更新成功")
        except:
            ConnO.conn.rollback() #发生错误时回滚
            print("语句执行错误")
        ConnO.conn.close()

        


if __name__ == "__main__":
    ConnO.read_data()
