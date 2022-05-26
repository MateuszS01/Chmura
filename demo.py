import mysql.connector

mydb = mysql.connector.connect(
  host="msbaza.database.windows.net",
  user="...",
  password="..."
)

print(mydb)