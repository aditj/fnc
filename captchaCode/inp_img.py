import sqlite3
import os
conn=sqlite3.connect("data.db")
cursor = conn.execute("SELECT sno,file_name FROM ads")
ls_photos=[]
sno=0
for i in cursor:
    ls_photos.append(i[1])
    sno=i[0]
print(ls_photos)
arr= os.listdir('/static/img')
print(arr)
sno+=1
for i in arr:
    if i in ls_photos:
        a=input("Enter The Answer for" + i)
        conn.execute("INSERT INTO ads VALUES(?,?,?)",(sno,i,a))
