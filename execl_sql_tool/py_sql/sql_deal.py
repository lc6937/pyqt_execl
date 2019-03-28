import pymysql
from execl_sql_tool.config.configInit import db_info

'''初始化连接串'''
def init_conn(database):
    host, port, user, password=db_info()
    conn = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database,
        charset="utf8")
    return conn

def connectTest():
    conn = init_conn("information_schema")# 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
    # 定义要执行的SQL语句
    sql ='select * from TABLES'
    # 执行SQL语句
    res=cursor.execute(sql)
    if res:
        return True
    else:
        return False


if __name__ == '__main__':
    res = connectTest()
    print(res)