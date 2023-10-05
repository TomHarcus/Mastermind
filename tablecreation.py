from mysql.connector import connect, Error

try:
    with connect(
            host="localhost",
            user="tom",
            password="Broughton123",
            database="mastermind",
    ) as connection:
        cursor = connection.cursor()
        create_highscore_table_query = """
        CREATE TABLE highscores(
        pos INT PRIMARY KEY,
        gamertag VARCHAR(4) NOT NULL,
        time FLOAT NOT NULL
        )
        """

        with connection.cursor() as cursor:
            cursor.execute(create_highscore_table_query)
            connection.commit()
except Error as e:
    print(e)