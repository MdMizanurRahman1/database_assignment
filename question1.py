import mysql.connector

# Connect to the database
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='airports',
    user='root',
    password='2217',
    autocommit=True
)

user_icao_code = input("Enter the ICAO code of an airport: ")
cursor = connection.cursor()

sql = f"select name, municipality from airports where ident='{user_icao_code}'"
cursor.execute(sql)
result = cursor.fetchone()

if result:
    print(f"Airport Name: {result[0]}")
    print(f"Location (Town): {result[1]}")
else:
    print("No airport found with that ICAO code.")
