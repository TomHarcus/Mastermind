# Import modules pygame, connect and Error
import pygame
from mysql.connector import connect, Error

# Create class
class Leaderboard():
    # Constructor function
    def __init__(self):
        self.leaderboard = []

    # Create method to update the database with a new highscore
    def update_database(self, connection):
        # Bubble sort to sort the leaderboard when a new time is added
        length = len(self.leaderboard)
        swaps = True
        while swaps != False:
            swaps = False
            for i in range(length - 1):
                gamertag1 = self.leaderboard[i][1]
                time1 = self.leaderboard[i][2]

                gamertag2 = self.leaderboard[i + 1][1]
                time2 = self.leaderboard[i + 1][2]
                if time1 > time2:
                    self.leaderboard[i + 1][1] = gamertag1
                    self.leaderboard[i + 1][2] = time1

                    self.leaderboard[i][1] = gamertag2
                    self.leaderboard[i][2] = time2
                    swaps = True
            length -= 1

        for i in range(len(self.leaderboard)):
            self.leaderboard[i] = tuple(self.leaderboard[i])

        # Initialises the query used
        delete_highscore_query = "DELETE FROM highscores"
        add_highscore_query = """
                                INSERT
                                INTO
                                highscores
                                (pos, gamertag, time)
                                VALUES( %s, %s, %s)
                                """
        # Connects to the database and runs the query
        with connection.cursor() as cursor:
            cursor.execute(delete_highscore_query)
            connection.commit()
            cursor.executemany(add_highscore_query, self.leaderboard)
            connection.commit()

    # Creates method to get the data from the database
    def get_data(self, player_data):
        # Tries and connects to the database
        try:
            with connect(
                host="localhost",
                user="tom",
                password="Broughton123",
                database="mastermind",
            ) as connection:
                cursor = connection.cursor()
                self.leaderboard = []
                # If connects it runs the query
                select_highscores_query = "SELECT * FROM highscores"
                with connection.cursor() as cursor:
                    cursor.execute(select_highscores_query)

                    result = cursor.fetchall()
                    # Checks if the players time is quicker than the slowest time in the leaderboard
                    if player_data[2] < result[9][2]:
                        # If yes, it adds it to the last place in the leaderbaord
                        result[9] = player_data
                        player_data[0] = 10
                    for record in result:
                        self.leaderboard.append(list(record))
                    # Calls the method to sort the leaderboard
                    self.update_database(connection)
        except Error as e:
            print(e)

    # Creates method to display the leaderboard
    def show_leaderboard(self, screen, black, check_guessed, anti_cheat):
        if check_guessed == False or anti_cheat == True:
            try:
                with connect(
                        host="localhost",
                        user="tom",
                        password="Broughton123",
                        database="mastermind",
                ) as connection:
                    cursor = connection.cursor()
                    self.leaderboard = []

                    select_highscores_query = "SELECT * FROM highscores"
                    with connection.cursor() as cursor:
                        cursor.execute(select_highscores_query)

                        result = cursor.fetchall()

                        for record in result:
                            self.leaderboard.append(list(record))

            except Error as e:
                print(e)

        font_display = pygame.font.Font("freesansbold.ttf", 30)
        for i in range(len(self.leaderboard)):
            screen.blit(font_display.render(
                str(self.leaderboard[i][0]) + "   " + str(self.leaderboard[i][1]) + "   " + str(self.leaderboard[i][2]) + " seconds", True, black), (65, 77 + (i * 63)))