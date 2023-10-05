from mysql.connector import connect, Error

try:
    with connect(
            host="localhost",
            user="tom",
            password="Broughton123",
            database="mastermind",
    ) as connection:
        cursor = connection.cursor()
        add_initial_data_query = """
        INSERT INTO highscores (pos, gamertag, time)
        VALUES 
            (1, "Null", 99999),
            (2, "Null", 99999),
            (3, "Null", 99999),
            (4, "Null", 99999),
            (5, "Null", 99999),
            (6, "Null", 99999),
            (7, "Null", 99999),
            (8, "Null", 99999),
            (9, "Null", 99999),
            (10, "Null", 99999)
        """

        with connection.cursor() as cursor:
            cursor.execute(add_initial_data_query)
            connection.commit()

except Error as e:
    print(e)