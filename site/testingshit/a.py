from sqlite3 import connect
def get_api_detail(user_id):
    conn =connect("data")
    curs = conn.execute("select api_id,nos,href from api_keys where user_id=?",(user_id,))
    api_details=[]
    for i in curs:
        api_details.append(i)
    return api_detail
conn =connect("data")
print(conn.execute("SELECT COUNT(key) FROM adverts").fetchone())
