import cx_Oracle
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


    def read_data():
        cursor = ConnO.conn.cursor()
        cursor.execute("select * from tb_user")
        #读取整个表格
        one = cursor.fetchall()
        return one

    
        


if __name__ == "__main__":
    ConnO()
    print()
