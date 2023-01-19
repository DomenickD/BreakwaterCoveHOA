import mysql.connector

cnx = mysql.connector.connect(user='username', password='password',
                              host='hostname',
                              database='myDB')

cursor = cnx.cursor()

query = ("SELECT id, firstname, lastname FROM MyGuests")

cursor.execute(query)

for (id, firstname, lastname) in cursor:
  print(f"id: {id}, name: {firstname} {lastname}")

cursor.close()
cnx.close()
