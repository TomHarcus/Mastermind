from mysql.connector import connect, Error

try:
    with connect(
            host="localhost",
            user="tom",
            password="", # Insert Password
            database="mastermind",
    ) as connection:
        cursor = connection.cursor()
        create_database_query = "CREATE DATABASE mastermind"
        with connection.cursor as cursor:
            cursor.execute(create_database_query)
except Error as e:
    print(e)