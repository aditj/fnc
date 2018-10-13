from sqlite3 import connect
def get_api_detail(user_id):
    conn =connect("data")
    return list(conn.execute("select api_id,nos,href from api_keys where user_id=?",(user_id,)))



def get_name(user_id):
    try:
        conn =connect('data')
        return conn.execute("select user_id from advertisee_user where user_id= ?",(user_id,)).fetchone()[0]
    except:
        return "N.A.U."
