from sqlite3 import connect
def checkhash(user_id,hash):
    conn= connect('data')

    hash_t=conn.execute("select pass_hash from advertisee_user where user_id= ?",(user_id,)).fetchone()
    
    conn.close()
    if hash_t==None:
        return False
    elif str(hash)==str(hash_t[0]):
        return True
    else :
        return False
