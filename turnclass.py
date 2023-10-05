# Import the module pygame
import pygame

# Create class
class Turn():
    # Constructor function
    def __init__(self, try_num, y_pos, reset, y_pos_pin_1, y_pos_pin_2, turnfont, displayanswer, namex, namey, circley, answerx, answery1, answery2, answerbackgroudx, answerbackgroundy, number, move):
        self.try_num = try_num
        self.y_pos = y_pos
        self.reset = reset
        self.y_pos_pin_1 = y_pos_pin_1
        self.y_pos_pin_2 = y_pos_pin_2
        self.turnfont = turnfont
        self.displayanswer = displayanswer
        self.namex = namex
        self.namey = namey
        self.circley = circley
        self.answerx = answerx
        self.answery1 = answery1
        self.answery2 = answery2
        self.answerbackgroundx = answerbackgroudx
        self.answerbackgroundy = answerbackgroundy
        self.number = number
        self.move = move
        self.turn_num = 0
        self.display_colours = []
        self.checked = False
        self.pins = []

    # Create method to display users guesses and clues
    def displaying(self, screen, black, white):
        if self.turn_num <= 4:
            for i in range(len(self.display_colours)):
                pygame.draw.circle(screen, self.display_colours[i], ((i + 1) * 45, self.y_pos), 20)

        if self.reset == False:
            for i in range(len(self.pins)):
                if i == 0 or i == 1:
                    if self.pins[i] == "1":
                        pygame.draw.circle(screen, black, (235 + ((i % 2) * 30), self.y_pos_pin_1), 10)
                    elif self.pins[i] == "2":
                        pygame.draw.circle(screen, white, (235 + ((i % 2) * 30), self.y_pos_pin_1), 10)
                elif i == 2 or i == 3:
                    if self.pins[i] == "1":
                        pygame.draw.circle(screen, black, (235 + ((i % 2) * 30), self.y_pos_pin_2), 10)
                    elif self.pins[i] == "2":
                        pygame.draw.circle(screen, white, (235 + ((i % 2) * 30), self.y_pos_pin_2), 10)

    # Create method to allow player to make guesses and remove guesses
    def pick_code(self, mousex, mousey, guess_colours, guesses, RED, BLUE, GREEN, YELLOW, ORANGE, PURPLE):
        if mousex >= 330 and mousex <= 390 and mousey >= 550 and mousey <= 610 and self.try_num == True:
            self.display_colours.append(RED)
            guess_colours.append("red")
            self.turn_num += 1
            guesses[0] += 1

        # Blue button
        elif mousex >= 410 and mousex <= 470 and mousey >= 550 and mousey <= 610 and self.try_num == True:
            self.display_colours.append(BLUE)
            guess_colours.append("blue")
            self.turn_num += 1
            guesses[1] += 1

        # Green button
        elif mousex >= 330 and mousex <= 390 and mousey >= 615 and mousey <= 675 and self.try_num == True:
            self.display_colours.append(GREEN)
            guess_colours.append("green")
            self.turn_num += 1
            guesses[2] += 1

        # Yellow button
        elif mousex >= 410 and mousex <= 470 and mousey >= 615 and mousey <= 675 and self.try_num == True:
            self.display_colours.append(YELLOW)
            guess_colours.append("yellow")
            self.turn_num += 1
            guesses[3] += 1

        # Orange button
        elif mousex >= 330 and mousex <= 390 and mousey >= 680 and mousey <= 740 and self.try_num == True:
            self.display_colours.append(ORANGE)
            guess_colours.append("orange")
            self.turn_num += 1
            guesses[4] += 1

        # Purple  button
        elif mousex >= 410 and mousex <= 470 and mousey >= 680 and mousey <= 740 and self.try_num == True:
            self.display_colours.append(PURPLE)
            guess_colours.append("purple")
            self.turn_num += 1
            guesses[5] += 1

        # Back arrow
        elif mousex >= 340 and mousex <= 455 and mousey >= 190 and mousey <= 270:
            if self.try_num == True and len(guess_colours) > 0:
                self.display_colours.pop()
                num = guess_colours.pop()
                self.turn_num -= 1
                if num == "red":
                    guesses[0] -= 1
                elif num == "blue":
                    guesses[1] -= 1
                elif num == "green":
                    guesses[2] -= 1
                elif num == "yellow":
                    guesses[3] -= 1
                elif num == "orange":
                    guesses[4] -= 1
                elif num == "purple":
                    guesses[5] -= 1


