from sqlite3 import connect
from random import randint




def increasecount(api_id):
    conn = connect('data')
    conn.execute("UPDATE api_keys SET nos = nos + 1 WHERE api_id = ?",(api_id,))
    conn.execute("UPDATE adverts SET n = n+1 WHERE key=? ",(img_key,))
    conn.commit()
    conn.close()
def url(api_id):
    conn = connect('data')
    return str(conn.execute("SELECT href FROM api_keys WHERE api_id=?",(api_id,)).fetchone()[0])
def get_image():
    conn = connect('data')
    leng=conn.execute("SELECT COUNT(key) FROM adverts").fetchone()[0]
    n= randint(1,leng)
    cursor = conn.execute("SELECT img_src,ans,key FROM adverts where key = ?",(n,))
    return cursor.fetchone()
def check_api(api_id):
    conn = connect('data')
    if len(conn.execute("SELECT api_id from api_keys where api_id = ?",(api_id,)).fetchall())!=0:
        return True
    else :
        return False
