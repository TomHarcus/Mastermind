# Import modules pygame and time
import pygame
import time

# Import subprograms
from setupclass import Setup
from turnclass import Turn
from screenclass import Screen
from database import Leaderboard

# Setup
pygame.init() # Initialise pygame
screen = pygame.display.set_mode((500,750)) # Initialise screen size and store in variable
pygame.display.set_caption("Mastermind") # Initialise title

# Global variables
pick_gamertag = True
start = False
pick_code = False
main = False
game_over = False
game_over_loss = False
last_guess = False
time_shown = False
add_database = False
display_leaderboard = False
anti_cheat = False
gamertag = ""

# Set colours
RED = (200,0,0)
BLUE = (0,0,200)
GREEN = (0,200,0)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
PURPLE = (148,0,211)
BLACK = (0,0,0)
WHITE = (255,255,255)
GREY = (169,169,169)

# Store colour variables in array
display_colours = [RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE]

# Set colour arrays
colours = []
guess_colours = []

# Set occurrence variables
colour_numbers = [0, 0, 0, 0, 0, 0]
guesses = [0, 0, 0, 0, 0, 0]
list_colours = ["red", "blue", "green", "yellow", "orange", "purple"]

# Initialise colour code
colour_code = []
amount = 0
num_turns = 0

# Create instances of the classes
setup = Setup()
board = Screen()
data = Leaderboard()

# Initialise turns
turn1 = Turn(True, 725, True, 707, 737, pygame.font.Font("freesansbold.ttf", 15), None, 14, 533, 540, 130, 537, 545, 126, 533, 1, 0)
turn2 = Turn(False, 660, False, 645, 675, pygame.font.Font("freesansbold.ttf", 15), None, 190, 533, 540, 306, 537, 545, 302, 533, 2, 175)
turn3 = Turn(False, 595, False, 580, 610, pygame.font.Font("freesansbold.ttf", 15), None, 340, 533, 540, 456, 537, 545, 452, 533, 3, 325)
turn4 = Turn(False, 530, False, 518, 548, pygame.font.Font("freesansbold.ttf", 15), None, 14, 583, 590, 130, 587, 595, 126, 583, 4, 0)
turn5 = Turn(False, 470, False, 457, 487, pygame.font.Font("freesansbold.ttf", 15), None, 190, 583, 590, 306, 587, 595, 302, 583, 5, 175)
turn6 = Turn(False, 410, False, 390, 420, pygame.font.Font("freesansbold.ttf", 15), None, 340, 583, 590, 456, 587, 595, 452, 583, 6, 325)
turn7 = Turn(False, 345, False, 328, 358, pygame.font.Font("freesansbold.ttf", 15), None, 14, 633, 640, 130, 637, 645, 126, 633, 7, 0)
turn8 = Turn(False, 280, False, 265, 295, pygame.font.Font("freesansbold.ttf", 15), None, 190, 633, 640, 306, 637, 645, 302, 633, 8, 175)
turn9 = Turn(False, 215, False, 205, 235, pygame.font.Font("freesansbold.ttf", 15), None, 340, 633, 640, 456, 637, 645, 452, 633, 9, 325)
turn10 = Turn(False, 150, False, 142, 172, pygame.font.Font("freesansbold.ttf", 15), None, 14, 683, 690, 130, 687, 695, 126, 683, 10, 0)
turn11 = Turn(False, 85, False, 78, 108, pygame.font.Font("freesansbold.ttf", 15), None, 190, 683, 690, 306, 687, 695, 302, 683, 11, 175)
turn12 = Turn(False, 20, False, 25, 55, pygame.font.Font("freesansbold.ttf", 15), None, 340, 690, 690, 456, 687, 695, 452, 683, 12, 325)

# Initialise an array of objects
turns_array = [turn1, turn2, turn3, turn4, turn5, turn6, turn7, turn8, turn9, turn10, turn11, turn12]

# Set main loop variable to true
running = True

# Main game loop
while running:
    # Sets game to pick gamertag screen
    if pick_gamertag == True:
        # Resets colour occurences array
        colour_occurences = [0, 0, 0, 0, 0, 0]
        # Sets background to white
        screen.fill(WHITE)
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.QUIT
            # Checks if user has pressed a key
            if event.type == pygame.KEYDOWN:
                # If users presses backspace it removes a letter from gamertag
                if event.key == pygame.K_BACKSPACE:
                    gamertag = gamertag[:-1]
                # Before adding the chosen letter to the gamertag it checks if its length is less than 4
                else:
                    if len(gamertag) < 4:
                        gamertag += event.unicode
            # Gets the position of the cursor when the left mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                # Checks if submit button is pressed
                if mousex >= 100 and mousex <= 300 and mousey >= 200 and mousey <= 300:
                    if len(gamertag) == 4:
                        start = True
                        pick_gamertag = False

        # Initialises and displays the "Please type in your gamertag:" text on screen
        gamertag_font = pygame.font.Font("freesansbold.ttf", 30)
        gamertag_explanation = gamertag_font.render("Please type in your gamertag:", True, BLACK)
        screen.blit(gamertag_explanation, (10, 55))

        # Initialises and displays the players gamertag on screen
        player_gamertag_font = pygame.font.Font("freesansbold.ttf", 50)
        player_gamertag = player_gamertag_font.render(gamertag, True, BLACK)
        screen.blit(player_gamertag, (150,120))

        # Displays the "Submit" button on screen
        pygame.draw.rect(screen, GREY, (150, 200, 200, 100))
        submit_font = pygame.font.Font("freesansbold.ttf", 30)
        submit = submit_font.render("Submit", True, BLACK)
        screen.blit(submit, (190, 235))

        # Updates the screen
        pygame.display.update()

    # Start screen
    if start == True:
        # Sets background to white
        screen.fill(WHITE)

        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.QUIT

            # Gets the position of the cursor when the left mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos

                # Checks if player presses "Play vs computer" button
                if mousex >= 100 and mousex <= 400 and mousey >= 450 and mousey <= 550:
                    # Generates a random 4 colour code by calling this method
                    setup.generate_code_computer(list_colours, colour_code, display_colours, colour_occurences, colours)
                    # Stores the current time in seconds since January 1st 1970 in variable
                    start_time = time.time()
                    main = True
                    start = False
                # Checks if player presses "Play vs someone" button
                elif mousex >= 100 and mousex <= 400 and mousey >= 600 and mousey <= 700:
                    # Sets the pick code variable to true so the game know that someone needs to pick the code
                    pick_code = True
                    start = False

        # Stores the amount of each colour in the generated code
        for i in range(len(colour_occurences)):
            colour_numbers[i] = colour_occurences[i]

        # Calls the method to display the buttons
        board.draw_start_buttons(screen, GREY, BLACK)

        # Updates screen
        pygame.display.update()

    # Checks if someone has to pick a code
    if pick_code == True:
        # Stops the players time being recorded in the database as they can now cheat
        anti_cheat = True
        # Sets the background to white
        screen.fill(WHITE)
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.QUIT

            # Gets the position of the cursor when the left mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                # Checks if player presses the red button
                if mousex >= 190 and mousex <= 250 and mousey >= 550 and mousey <= 610 and amount < 4:
                    # Calls the method to add the colour to the code
                    setup.generate_code_player(colour_code, colours, colour_occurences, RED, "red", 0)
                    # Increments amount by 1
                    amount += 1
                # Checks if player presses the blue button
                elif mousex >= 270 and mousex <= 330 and mousey >= 550 and mousey <= 610 and amount < 4:
                    # Calls the method to add the colour to the code
                    setup.generate_code_player(colour_code, colours, colour_occurences, BLUE, "blue", 1)
                    # Increments amount by 1
                    amount += 1
                # Checks if player presses the green button
                elif mousex >= 190 and mousex <= 250 and mousey >= 615 and mousey <= 675 and amount < 4:
                    # Calls the method to add the colour to the code
                    setup.generate_code_player(colour_code, colours, colour_occurences, GREEN, "green", 2)
                    # Increments amount by 1
                    amount += 1
                # Checks if player presses the yellow button
                elif mousex >= 270 and mousex <= 330 and mousey >= 615 and mousey <= 675 and amount < 4:
                    # Calls the method to add the colour to the code
                    setup.generate_code_player(colour_code, colours, colour_occurences, YELLOW, "yellow", 3)
                    # Increments amount by 1
                    amount += 1
                # Checks if player presses the orange button
                elif mousex >= 190 and mousex <= 250 and mousey >= 680 and mousey <= 740 and amount < 4:
                    # Calls the method to add the colour to the code
                    setup.generate_code_player(colour_code, colours, colour_occurences, ORANGE, "orange", 4)
                    # Increments amount by 1
                    amount += 1
                # Checks if player presses the purple button
                elif mousex >= 270 and mousex <= 330 and mousey >= 680 and mousey <= 740 and amount < 4:
                    # Calls the method to add the colour to the code
                    setup.generate_code_player(colour_code, colours, colour_occurences, PURPLE, "purple", 5)
                    # Increments amount by 1
                    amount += 1
                # Checks if player presses the start button
                elif mousex >= 100 and mousex <= 400 and mousey >= 300 and mousey <= 400 and amount == 4:
                    # Stores the current time in seconds since January 1st 1970 in variable
                    start_time = time.time()
                    main = True
                    pick_code = False

            # Stores the amount of each colour in the generated code
            for i in range(len(colour_occurences)):
                colour_numbers[i] = colour_occurences[i]

        # Calls method to display the chosen code
        board.display_chosen_code(amount, colour_code, screen, GREY, BLACK)
        # Calls the method to display the colour buttons
        board.draw_pallet_setup(screen, RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE)
        # Updates screen
        pygame.display.update()

    # Main game
    if main == True:
        # Sets the background to white
        screen.fill(WHITE)
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.QUIT
            # Gets the position of the cursor when the left mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos

                # Loops through each turn
                for turn in turns_array:
                    # Calls the method to analyse each turn made by player
                    turn.pick_code(mousex, mousey, guess_colours, guesses, RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE)

                # Loops through each turn
                for turn in turns_array:
                    # Finds turn number
                    pos = turns_array.index(turn)

                    # Checks if player has made all 4 guesses of current turn
                    if turn.turn_num == 4:
                        # Checks if turn is current turn
                        if turn.reset == True:
                            for i in range(len(colour_numbers)):
                                # Stores the occurrences of each colour in array
                                colour_occurences[i] = colour_numbers[i]
                            # Sets the number of right colours to 0
                            right = 0

                            # Loops through players guess
                            for i in range(len(guess_colours)):
                                # Checks if any of the colours is in the right place
                                if guess_colours[i] == colours[i]:
                                    # Loops through guesses array
                                    for j in range(len(guesses)):
                                        # Checks that the colour in the code has not already been processed
                                        if guess_colours[i] == list_colours[j] and guesses[j] > 0:
                                            # Adds 1 to objects pins array
                                            turn.pins.append("1")
                                            # Takes 1 away from how many of that colour you have left
                                            colour_occurences[j] -= 1
                                            guesses[j] -= 1
                                            # Adds 1 to right variable
                                            right += 1

                            # Loops through players guess
                            for i in range(len(guess_colours)):
                                # Loops through colours array
                                for j in range(len(colours)):
                                    # Checks if player has guessed a right colour and its in a different position
                                    if guess_colours[i] == colours[j] and i != j:
                                        # Loops through list_colours array
                                        for k in range(len(list_colours)):
                                            # Checks that the colour in the code has not already been processed
                                            if guess_colours[i] == list_colours[k] and colour_occurences[k] > 0 and guesses[k] > 0:
                                                # Adds 2 to objects pins array
                                                turn.pins.append("2")
                                                guesses[k] -= 1
                                                # Takes 1 away from how many of that colour you have left
                                                colour_occurences[k] -= 1

                            # Checks if player has won
                            if right == 4:
                                game_over = True
                                main = False
                            # Checks if player has lost
                            elif pos == 11:
                                game_over_loss = True
                                main = False

                            # Resets necessary variables and arrays for next guess
                            guess_colours = []

                            for i in range(len(guesses)):
                                guesses[i] = 0

                            turn.try_num = False
                            if pos < 11:
                                turns_array[pos + 1].try_num = True
                                turns_array[pos + 1].reset = True
                            num_turns += 1
                            turn.reset = False

        # Draws everything om screen
        board.draw_grid(screen, GREY)
        board.draw_pallet(screen, RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE)
        for turn in turns_array:
            turn.displaying(screen, BLACK, WHITE)
        pygame.draw.rect(screen, GREY, (340, 190, 115, 80))
        arrow = pygame.image.load("arrow.png")
        screen.blit(arrow, (360, 200))
        # Updates screen
        pygame.display.update()

    # Checks if game is over
    if game_over == True or game_over_loss == True:
        # Sets background to white
        screen.fill(WHITE)
        # Checks for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.QUIT
            # Gets the position of the cursor when the left mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                # Checks if player presses restart button
                if mousex >= 40 and mousex <= 240 and mousey >= 280 and mousey <= 380:
                    # Resets all necessary variables and arrays for next player
                    colours = []
                    guess_colours = []

                    colour_code = []
                    amount = 0

                    num_turns = 0

                    pick_gamertag = True
                    game_over = False
                    game_over_loss = False
                    time_shown = False
                    add_database = False
                    gamertag = ""
                    for turn in turns_array:
                        turn.try_num = False
                        turn1.try_num = True
                        turn.turn_num = 0
                        turn.display_colours = []
                        turn.reset = False
                        turn1.reset = True
                        turn.checked = False
                        turn.pins = []

                # Checks if player presses leaderboard button
                if mousex >= 260 and mousex <= 460 and mousey >= 280 and mousey <= 380:
                    # Sets leaderboard variable to true
                    display_leaderboard = True
                    game_over = False
                    game_over_loss = False

            # Checks if player won the game
            if game_over == True:
                if time_shown == False:
                    # Calculates players time
                    player_time = round(time.time() - start_time, 2)
                    time_shown = True
                # Checks if time gets added to database
                if add_database == False and anti_cheat == False:
                    data.get_data([None, gamertag, player_time])
                    add_database = True

                # Displays all information on screen
                time_font_display = pygame.font.Font("freesansbold.ttf", 30)
                time_font = time_font_display.render("You took: " + str(player_time) + " seconds", True, BLACK)
                screen.blit(time_font, (10, 55))
                you_win_font = pygame.font.Font("freesansbold.ttf", 30)
                you_win = you_win_font.render("You have guessed correctly!", True, BLACK)
                you_win3_font = pygame.font.Font("freesansbold.ttf", 30)
                you_win3 = you_win3_font.render("Here was the code:", True, BLACK)
                screen.blit(you_win, (10, 10))
                if num_turns == 1:
                    you_win2_font = pygame.font.Font("freesansbold.ttf", 30)
                    you_win2 = you_win2_font.render("It took you " + str(num_turns) + " try", True, BLACK)
                else:
                    you_win2_font = pygame.font.Font("freesansbold.ttf", 30)
                    you_win2 = you_win2_font.render("It took you " + str(num_turns) + " tries", True, BLACK)

                screen.blit(you_win2, (10, 100))
                screen.blit(you_win3, (10, 150))

            # Checks if player lost
            elif game_over_loss == True:
                # Displays all information on screen
                you_lose_font = pygame.font.Font("freesansbold.ttf", 30)
                you_lose = you_lose_font.render("You have failed to guess the code!", True, BLACK)
                you_lose1_font = pygame.font.Font("freesansbold.ttf", 30)
                you_lose1 = you_lose1_font.render("Here was the right code:", True, BLACK)
                restart2_font = pygame.font.Font("freesansbold.ttf", 30)
                restart2 = restart2_font.render("Click to restart", True, BLACK)
                screen.blit(you_lose, (10, 50))
                screen.blit(you_lose1, (10, 100))


            restart_font = pygame.font.Font("freesansbold.ttf", 24)
            restart = restart_font.render("Click to restart", True, BLACK)

            highscore_font = pygame.font.Font("freesansbold.ttf", 21)
            highscore = highscore_font.render("See leaderboard", True, BLACK)

            # Displays code
            for i in range(len(colour_code)):
                pygame.draw.circle(screen, colour_code[i], ((i + 1) * 100, 220), 30)

            pygame.draw.rect(screen, GREY, (40, 280, 200, 100))
            pygame.draw.rect(screen, GREY, (260, 280, 200, 100))
            screen.blit(restart, (48, 320))
            screen.blit(highscore, (268, 320))

            answers_font = pygame.font.Font("freesansbold.ttf", 20)
            answers = answers_font.render("Your guesses:", True, BLACK)

            screen.blit(answers, (10, 500))

            # Displays players turns
            for turn in turns_array:
                turn.displayanswer = turn.turnfont.render(str(turn.number), True, BLACK)
                for i in range(len(turn.display_colours)):
                    screen.blit(turn.displayanswer, (turn.namex, turn.namey))
                    pygame.draw.circle(screen, turn.display_colours[i], (((i + 2) * 23) + turn.move, turn.circley), 10)

                if len(turn.pins) > 0:
                    pygame.draw.rect(screen, GREY, (turn.answerbackgroundx, turn.answerbackgroundy, 17, 17))

                for i in range(len(turn.pins)):
                    if i == 0 or i == 1:
                        if turn.pins[i] == "1":
                            pygame.draw.circle(screen, BLACK, (turn.answerx + ((i % 2) * 8), turn.answery1), 3)
                        elif turn.pins[i] == "2":
                            pygame.draw.circle(screen, WHITE, (turn.answerx + ((i % 2) * 8), turn.answery1), 3)
                    elif i == 2 or i == 3:
                        if turn.pins[i] == "1":
                            pygame.draw.circle(screen, BLACK, (turn.answerx + ((i % 2) * 8), turn.answery2), 3)
                        elif turn.pins[i] == "2":
                            pygame.draw.circle(screen, WHITE, (turn.answerx + ((i % 2) * 8), turn.answery2), 3)

            # Updates screen
            pygame.display.update()

    # Checks if the leaderboard should be displayed
    if display_leaderboard == True:
        # Sets background to white
        screen.fill(WHITE)
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.QUIT
            # Gets the position of the cursor when the left mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                # Checks if back button is pressed
                if mousex >= 100 and mousex <= 200 and mousey >= 700 and mousey <= 740:
                    if time_shown == True:
                        game_over = True
                        display_leaderboard = False
                    else:
                        game_over_loss = True
                        display_leaderboard = False
        # Displays information on screen
        data.show_leaderboard(screen, BLACK, time_shown, anti_cheat)
        pygame.draw.rect(screen, GREY, (100, 700, 100, 40))
        goback_font_display = pygame.font.Font("freesansbold.ttf", 30)
        goback_font = goback_font_display.render("Back", True, BLACK)
        screen.blit(goback_font, (110, 705))

        # Updates screen
        pygame.display.update()

