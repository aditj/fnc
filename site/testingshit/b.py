def helloboi():
    conn = sqlite3.connect(data.db)
    conn.execute("create table intt(no int primary key);")
    prii = conn.execute(".tables")
    print(prii)
