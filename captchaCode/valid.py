import sqlite3
conn = sqlite3.connect('data.db')

cursor = conn.execute("SELECT file_name,ans FROM ads")
dict_ans={}
for i in cursor:
    dict_ans[i[0]]=i[1]
flag=False
def valid(ans,file_name):
    if dict_ans[file_name]==ans:
        flag=True
        return flag
