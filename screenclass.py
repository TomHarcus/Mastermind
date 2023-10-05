# Import module pygame
import pygame

# Create class
class Screen():
    # Draws the start screen
    def draw_start_buttons(self, screen, grey, black):
        computer_font = pygame.font.Font("freesansbold.ttf", 25)
        computer = computer_font.render("Play vs the computer", True, (black))
        pygame.draw.rect(screen, grey, (100, 450, 300, 100))
        screen.blit(computer, (120, 485))

        person_font = pygame.font.Font("freesansbold.ttf", 30)
        person = person_font.render("Play vs someone", True, (black))
        pygame.draw.rect(screen, grey, (100, 600, 300, 100))
        screen.blit(person, (125, 635))

        title_font = pygame.font.Font("freesansbold.ttf", 50)
        title = title_font.render("Mastermind", True, black)
        screen.blit(title, (105,10))

        chair = pygame.image.load("mastermindchair.jpg")
        screen.blit(chair, (100, 120))

    # Draws the main grid
    def draw_grid(self, screen, grey):
        for i in range(12):
            pygame.draw.rect(screen, grey, (10, i*63, 200, 60))
            pygame.draw.rect(screen, grey, (220, i*63, 60, 60))

    # Setup Pallet
    def draw_pallet_setup(self, screen, red, blue, green, yellow, orange, purple):
        red_button = pygame.draw.circle(screen, red, (220,580), 30)
        blue_button = pygame.draw.circle(screen, blue, (300,580), 30)
        green_button = pygame.draw.circle(screen, green, (220,645), 30)
        yellow_button = pygame.draw.circle(screen, yellow, (300,645), 30)
        orange_button = pygame.draw.circle(screen, orange, (220,710), 30)
        purple_button = pygame.draw.circle(screen, purple, (300,710), 30)

    # Draws the colour pallet
    def draw_pallet(self, screen, red, blue, green, yellow, orange, purple):
        red_button = pygame.draw.circle(screen, red, (360,580), 30)
        blue_button = pygame.draw.circle(screen, blue, (440,580), 30)
        green_button = pygame.draw.circle(screen, green, (360,645), 30)
        yellow_button = pygame.draw.circle(screen, yellow, (440,645), 30)
        orange_button = pygame.draw.circle(screen, orange, (360,710), 30)
        purple_button = pygame.draw.circle(screen, purple, (440,710), 30)

    # Draws the chosen code by the other player
    def display_chosen_code(self, amount, colour_code, screen, GREY, BLACK):
        for i in range(len(colour_code)):
            pygame.draw.circle(screen, colour_code[i], ((i + 1) * 100, 210), 30)
        start_game_font = pygame.font.Font("freesansbold.ttf", 20)
        start_game = start_game_font.render("Click to start the game!", True, (BLACK))
        pygame.draw.rect(screen, GREY, (100, 300, 300, 100))
        screen.blit(start_game, (130, 335))

        explain_font = pygame.font.Font("freesansbold.ttf", 30)
        explain_font = explain_font.render("Choose a colour combintation:", True, BLACK)
        screen.blit(explain_font, (25, 50))
