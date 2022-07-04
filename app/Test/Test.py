import MSSQL

# ms=MSSQL.SqlsvLib()
# ll=ms.ExecNonQuery("insert into persons values(4,'jake','jake.M')")
# ll=ms.ExecSqlQuery("select * from persons")
# print(ll)

ms=MSSQL.SqlsvLib()
sql = 'select * from persons'
aa = ms.ExecSqlQuery(sql)
print(aa)
file_dict = dict(aa)
print(file_dict)