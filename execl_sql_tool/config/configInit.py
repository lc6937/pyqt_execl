from configparser import ConfigParser

'''实例化 configparser 并加载配置文件'''
def init_config():
    config = ConfigParser()
    config.read("init.conf", encoding='utf-8')
    return config

def db_info():
    config = init_config()
    dbinfo = []
    host=""
    port=""
    user=""
    password=""
    if config.has_section('db'):
        host = config.get('db', 'db_host')
        port = config.get('db', 'db_port')
        user = config.get('db', 'db_user')
        password = config.get('db', 'db_pass')
    return host,port,user,password

if __name__ == '__main__':
    host, port, user, password = db_info()
    print(host, port, user, password)