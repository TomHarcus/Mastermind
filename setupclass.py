# Import module random
import random

# Create class
class Setup():
    # Create method that generates a random code
    def generate_code_computer(self, list_colours, colour_code, display_colours, colour_occurences, colours):
        # Does a fixed loop
        for i in range(4):
            # Generates a random colour from a list
            colour = random.choice(list_colours)
            for j in range(len(list_colours)):
                if colour == list_colours[j]:
                    colour_code.append(display_colours[j])
                    colour_occurences[j] += 1
            # Add the colour to the array
            colours.append(colour)

    # Create method that gets player to pick a random code
    def generate_code_player(self, colour_code, colours, colour_occurences, display_colour, list_colour, num):
        colour_code.append(display_colour)
        colours.append(list_colour)
        colour_occurences[num] += 1


