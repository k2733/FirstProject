import pymssql

class SqlsvLib:
    def __init__(self):  # 类的构造函数，初始化数据库连接ip或者域名，以及用户名，密码，要连接的数据库名称
        self.sqhost = 'VPC2201010'        #sqhost在readconfig内声明
        self.squser = 'sa'        #squser在readconfig内声明
        self.sqpasswd = 'vcc2022!'        #sqpasswd在readconfig内声明
        self.sqdb = 'vcc'       #sqdb在readconfig内声明

    def __GetSqlConnect(self):  # 得到数据库连接信息函数， 返回: conn.cursor()
        self.conn = pymssql.connect(host=self.sqhost, user=self.squser, password=self.sqpasswd, database=self.sqdb, charset='utf8')
        sqcur = self.conn.cursor()  # 将数据库连接信息，赋值给cur。
        if not sqcur:
            return (NameError, "sqlserver连接数据库失败")
        else:
            return sqcur

    # 执行查询语句,返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    def ExecSqlQuery(self, sql):  # 执行Sql语句函数，返回结果
        sqcur = self.__GetSqlConnect()  # 获得数据库连接信息
        # 使用execure方法执行sql语句
        try:
            sqcur.execute(sql)  # 执行Sql语句
            resList = sqcur.fetchall()  # 获得所有的查询结果
        except:
            print("Error:sql unable to fetch data")
        self.conn.close()  # 查询完毕后必须关闭连接
        return resList      # 返回查询结果

    def ExecNonQuery(self, sql):
        sqcur = self.__GetSqlConnect()
        sqcur.execute(sql)
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    ms=SqlsvLib()
    ll=ms.ExecSqlQuery("select  * from  persons")
    print(ll)