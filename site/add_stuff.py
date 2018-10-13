from sqlite3 import connect
from random import choice
import string

def register(name,user_id,pass_hash,email):
    conn=connect("data")
    conn.execute("INSERT INTO advertisee_user VALUES(?,?,?,?)",(user_id,name,pass_hash,email,))
    conn.commit()
    conn.close()
def add_api(user_id,url):
    conn=connect("data")
    print("success0")
    length =16
    api = ''.join(choice(string.ascii_letters + string.digits) for _ in range(length))
    while len(conn.execute("SELECT api_id from api_keys where api_id = ?",(api,)).fetchall())!=0:
        api = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
    conn.execute("INSERT INTO api_keys VALUES(?,?,?,?)",(api,0,url,user_id,))
    print("success")
    conn.commit()
    conn.close()
    return True
