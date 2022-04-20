import psycopg2


# connect to "chinook" database
connection = psycopg2.connect(database="chinook")

# build a cursor object of the database
cursor = connection.cursor()

# Queries
# cursor.execute('SELECT * FROM "Artist"')
# cursor.execute('SELECT "Name" FROM "Artist"')
# cursor.execute('SELECT * FROM "Artist" WHERE "Name" = %s', ["Queen"])
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

# fetch the results
results = cursor.fetchall()
for result in results:
    if len(results) > 2:
        print(result)
    else:
        results = cursor.fetchone()
        print(result)

# close the connection
connection.close()
