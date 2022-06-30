import cx_Oracle

tns = cx_Oracle.makedsn("dx.huangyi.cn","1521","orcl")  #监听Oracle数据库
# 建立和数据库系统的连接
conn = cx_Oracle.connect("C##VCC","VCC",tns)   #连接数据库


'''
1.新建tb_user表,表结构:id number, name varchar2(50),password varchar(50)  primary key(id)
2.给表插入几行数据
3.查询数据
'''



#1.建新表
#获取操作游标
# cursor = conn.cursor()
# #执行SQL，创建一个表
# cursor.execute("create table tb_user(id number, name varchar2(50),password varchar(50),primary key(id))")
# #关闭连接，释放资源
# cursor.close()
# #执行完成，打印提示信息
# print("successful")



# #2.插入一条数据
# cursor = conn.cursor()
# cursor.execute("insert into tb_user values(1,'admin','password')")
# #再插入一条数据
# param = {"id":2,"n":"admin",'p':"password"}
# cursor.execute("insert into tb_user values(:id,:n,:p)",param)
# #一次插入多条数据数据，参数为字典列表形式
# param = [{"id":3,"n":"admin","p":"password"},{"id":4,"n":"admin","p":"password"}]
# cursor.executemany("insert into tb_user values(:id,:n,:p)",param)
# #再一次插入多条数据
# param = []
# #生成6条插入数据，参数为元组列表形式
# for i in range(6,12):
#     param.append((i,"user"+str(i),"password"+str(i)))
# # 插入数据
# cursor.executemany("insert into tb_user values(:1,:2,:3)",param)
# cursor.close()
# #提交更改
# conn.commit()
# conn.close()



#3.查询数据
cursor = conn.cursor()
cursor.execute("select * from tb_user")
#获取一条记录
one = cursor.fetchall()
print(one)
conn.close()
