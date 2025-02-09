import csv
import sqlite3

conn=sqlite3.connect("jarvis.db")
cursor=conn.cursor()

query="create table if not exists sys_command(id integer primary key, name varchar(100),path varchar(1000))"
cursor.execute(query)
query="insert into sys_command values(null,'one note','C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
cursor.execute(query)

query="create table if not exists web_command(id integer primary key, name varchar(100), path varchar(1000))"
cursor.execute(query)
query="insert into web_command values(null,'youtube','https://www.youtube.com/')"
cursor.execute(query)

# query="create table if not exists contacts (id integer primary key, name varchar(200), mobile_no varchar(255), email varchar(255) NULL)"
# cursor.execute(query)

# desired_columns_indices = [0, 20]
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#      csvreader = csv.reader(csvfile)
#      for row in csvreader:
#          selected_data = [row[i] for i in desired_columns_indices]
#          cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))
conn.commit()
conn.close()
