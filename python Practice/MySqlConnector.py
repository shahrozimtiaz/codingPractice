import MySQLdb

conn = None
cursor = None

def connect(hostName,passw):
    conn = MySQLdb.connect('localhost',user=hostName, password=passw, db='python')
    print('Connected to',conn.get_host_info())
    cursor = conn.cursor()
    return cursor

def close():
    if(conn!=None and cursor!=None):
        conn.close()
        cursor.close()
