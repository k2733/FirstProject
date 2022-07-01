# coding:utf-8
import cx_Oracle
file_dict = {}

tns = cx_Oracle.makedsn("dx.huangyi.cn","1521","orcl")  #监听Oracle数据库
conn = cx_Oracle.connect("C##VCC","VCC",tns)   #连接数据库

# file => dict
def file_read():
    tns = cx_Oracle.makedsn("dx.huangyi.cn","1521","orcl")  #监听Oracle数据库
    conn = cx_Oracle.connect("C##VCC","VCC",tns)   #连接数据库
    with open('user.txt') as f:
        cursor = conn.cursor()
        cursor.execute("select * from tb_user")
        #读取整个表格到字典file_dict
        file_dict = dict(cursor.fetchall())
    conn.close() 
    return file_dict

# ditc => file
def file_write(username,password):
    tns = cx_Oracle.makedsn("dx.huangyi.cn","1521","orcl")  #监听Oracle数据库
    conn = cx_Oracle.connect("C##VCC","VCC",tns)
    cursor = conn.cursor()
        #更新密码，
    sql = "update tb_user set password = '%s' WHERE name = '%s'" %(password,username)
    try:
            cursor.execute(sql)
            conn.commit() 
            print("数据更新成功")
    except:
            conn.rollback() #发生错误时回滚
            print("语句执行错误")
    conn.close()
    

if __name__ == "__main__":
    print(file_dict)
