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

user_area_code = input('Enter your area code with capital letters: ')

cursor = connection.cursor()

sql=f"""
    SELECT type, COUNT(*) 
    FROM airports
    WHERE iso_country = '{user_area_code}'
    GROUP BY type
    ORDER BY type ASC
"""
cursor.execute(sql)

result = cursor.fetchall()


if result:
    print(f"Airports in country {user_area_code}:")
    for row in result:
        print(f"{row[0]}: {row[1]}")
else:
    print(f"No airports found for country code '{user_area_code}'.")
