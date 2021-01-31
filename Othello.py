# Importing modules
import pygame
import numpy as np
import random

# Initializing the Pygame module
pygame.init()


def console_screen():
    """This function is meant for the user to enter specifications for the game as the player plays. """
    print('Note: Enter nicknames to name the players in the game')
    user = ''
    user2 = ''
    try:
        user = input("Enter the name of player 1(Enter 'Computer 1' if you don't want to be named): ")
        user2 = input("Enter the name of player 2(Enter 'Computer 2' if there is no other player): ")
        print('1 Minecraft Music Remix\n'
              '2 Minecraft Calm Music\n'
              '3 No Music')
        music = input('Pick an option for music: ')
        if music == '1':
            pygame.mixer_music.load('MinecraftThemeSong.mp3')
            pygame.mixer.music.set_volume(.1)
            pygame.mixer_music.play(loops=100, start=0.0)
        elif music == '2':
            pygame.mixer_music.load('MinecraftThemeSong2.mp3')
            pygame.mixer_music.play(loops=100, start=0.0)
        elif music == '3':
            pass
        else:
            raise ValueError

    except ValueError:  # Except statement for invalid user input
        music = ''
        while music != '1' or music != '2' or music != '3':
            print('Invalid input. Please enter a valid choice')
            print('1 Minecraft Music Remix\n'
                  '2 Minecraft Calm Music\n'
                  '3 No Music')
            music = input('Pick an option for music: ')
            if music == '1':
                pygame.mixer_music.load('MinecraftThemeSong.mp3')
                pygame.mixer.music.set_volume(.1)
                pygame.mixer_music.play(loops=100, start=0.0)
                break
            elif music == '2':
                pygame.mixer_music.load('MinecraftThemeSong2.mp3')
                pygame.mixer_music.play(loops=100, start=0.0)
                break
            elif music == '3':
                break
    except IOError:  # Except statement if a file could not be opened
        print('Could not open file. File may not exist')
    except AttributeError:  # Except statement if a module is not found
        print('No module found.')
    return user, user2


# Setting up Pygame Display window
display_width = 800
display_height = 600

# Defining colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 220, 0)
LIGHTER_GREEN = (0, 255, 0)
DARK_GREEN = (0, 150, 0)
BLUE = (0, 100, 100)
LIGHTER_BLUE = (0, 128, 128)
ORANGE = (255, 150, 0)
LIGHTER_ORANGE = (255, 165, 0)
YELLOW = (235, 235, 0)
LIGHTER_YELLOW = (255, 255, 0)

# Game Initialization and Settings
name1, name2 = console_screen()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('OTHELLO GAME')
clock = pygame.time.Clock()
click = pygame.mouse.get_pressed()
mouse = pygame.mouse.get_pos()

# Images used in the game
OthelloImage = pygame.image.load('reversi.png')
DirectionsImage = pygame.image.load('directions2.png')
Othello_background_image = pygame.image.load('background_othello_image.png')
Wood_background = pygame.image.load('wood_background.png')

# Dimensions of the board
rows = 8
columns = 8

# Circle Radius
circle_radius = int((40 / 2) - 2)


# Displaying the Othello Image
def othello_image(x, y):
    """ This function adds an image of the Othello board to the pygame display.
    It takes coordinates to place the image and the pygame display shows it. """
    gameDisplay.blit(OthelloImage, (x, y))


# Displaying the Directions Image
def directions_image(x, y):
    """This function adds an image of the Othello instructions to the pygame display.
    It takes coordinates to place the image and the pygame display shows it."""
    gameDisplay.blit(DirectionsImage, (x, y))


# Displaying the Background Othello Image
def background_othello_image(x, y):
    """This function adds an image of an Othello background to the pygame display.
    It takes coordinates to place the image and the pygame display shows it."""
    gameDisplay.blit(Othello_background_image, (x, y))


# Displaying the Wood Background Image
def wood_background_image(x, y):
    """This function adds an image of a Wood Background to the pygame display.
    It takes coordinates to place the image and the pygame display shows it."""
    gameDisplay.blit(Wood_background, (x, y))


# Creating the board
def game_board():
    """This function creates a matrix of zeros to create the board."""
    board = np.zeros((rows, columns))
    return board


def piece_placed(x, y, player, board):
    """This function determines the piece played.
    It takes the coordinates of the piece, the player number, and the board.
    The pieces are zeros or ones and the function returns the piece on the board based on the number."""
    if player == 0:
        board[x][y] = 1
    elif player == 1:
        board[x][y] = 2
    return board


# Reversing the order of array elements along the specified axis
def print_board(board):
    """This function reverses the order of array elements along the specified axis.
    It takes the game board and prints a reversed version after a move."""
    print(np.flip(board, 0))


# Assigning the board to the variable board
board = game_board()


# Function to create text objects
def text_objects(text, font, color):
    """This function creates text objects in the pygame display.
    It takes a string, a font and a color for the text and it returns a variable with the details about the text. """
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


# Displaying the first intro text
def message_display(text, color):
    """This function creates the first intro text.
    It takes the text_objects function and color, and it displays it in the pygame display."""
    largeText = pygame.font.Font('freesansbold.ttf', 35)
    TextSurface, TextRectangle = text_objects(text, largeText, color)
    TextRectangle.center = ((display_width / 2), (display_height / 1.2))
    gameDisplay.blit(TextSurface, TextRectangle)
    # pygame.display.update()
    # time.sleep(2)
    # game_loop()


# Displaying the second intro text
def message_display2(text, color):
    """This function creates the second intro text.
    It takes the text_objects function and color, and it displays it in the pygame display."""
    largeText = pygame.font.Font('freesansbold.ttf', 45)
    TextSurface, TextRectangle = text_objects(text, largeText, color)
    TextRectangle.center = ((display_width / 2), (display_height / 4.5))
    gameDisplay.blit(TextSurface, TextRectangle)


# Message display for the scoreboard and Othello title
def message_display3(text, color):
    """This function creates the Othello text.
    It takes the text_objects function and color, and it displays it in the pygame display."""
    largeText = pygame.font.Font('times new roman.ttf', 45)
    TextSurface, TextRectangle = text_objects(text, largeText, color)
    TextRectangle.center = (280, 540)
    gameDisplay.blit(TextSurface, TextRectangle)


# Displaying the Player win text
def winner_or_tie_text(text, color):
    """This function creates a text for the winner.
    It takes the text_objects function and color, and it displays it in the pygame display."""
    largeText = pygame.font.Font('times new roman.ttf', 70)
    TextSurface, TextRectangle = text_objects(text, largeText, color)
    TextRectangle.center = ((display_width / 2), (display_height / 9))
    gameDisplay.blit(TextSurface, TextRectangle)


# Displaying the return text
def return_text(text, color):
    """This function creates a text to return to the main menu.
    It takes the text_objects function and color, and it displays it in the pygame display."""
    largeText = pygame.font.Font('freesansbold.ttf', 15)
    TextSurface, TextRectangle = text_objects(text, largeText, color)
    TextRectangle.center = ((display_width / 1.2), (display_height / 1.05))
    gameDisplay.blit(TextSurface, TextRectangle)


# Button function
def button(message, x, y, width, height, inactive_color, active_color, action=None):
    """This function creates the buttons for the main menu. It takes a text for the button, the measurements, the color, and a boolean.
    It creates the buttons in the pygame display and assigns them an action when clicked."""
    color = BLACK
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    # print(click)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))

    # Creating text for the buttons
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    textSurface, textRectangle = text_objects(message, smallText, color)
    textRectangle.center = ((x + (width/2)), (y+(height/2)))
    gameDisplay.blit(textSurface, textRectangle)


# Intro Screen
def game_intro():
    """This function creates the intro of the game with the Othello image, name of the game, and
    an action to start when the code is run."""
    x = 0
    y = 0
    gameDisplay.fill(WHITE)
    othello_image(x, y)
    message_display('Press Space to Play', BLACK)
    message_display2('REVERSI (OTHELLO)', BLACK)
    pygame.display.update()
    intro = False
    while not intro:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    second_display()
                    intro = True


# Second Screen
def second_display():
    """This function creates the second display after the intro.
    It displays a background image, the buttons of the main menu, and actions when clicked. """
    x = 0
    y = 0
    gameDisplay.fill(WHITE)
    background_othello_image(x, y)
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
        button('Player VS Player', 200, 115, 400, 70, BLUE, LIGHTER_BLUE, player_player)
        button('Player VS Computer', 200, 200, 400, 70, ORANGE, LIGHTER_ORANGE, player_computer)
        button('Computer VS Computer', 200, 285, 400, 70, YELLOW, LIGHTER_YELLOW, computer_computer)
        button('How To Play', 200, 370, 400, 70, GREEN, LIGHTER_GREEN, how_to_play)
        pygame.display.update()
        clock.tick(60)


def display_board():
    """This function creates a board display. It creates eight columns with eight rows of squares for the board.
    It indicates the text, size, color, and action."""
    x = 0
    y = 0
    wood_background_image(x, y)
    # gameDisplay.fill(RED)
    button('', 90, 90, 413, 413, BLACK, BLACK, None)
    # 1st column of boxes
    button('', 100, 450, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 100, 400, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 100, 350, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 100, 300, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 100, 250, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 100, 200, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 100, 150, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 100, 100, 40, 40, DARK_GREEN, DARK_GREEN, None)

    # 2st column of boxes
    button('', 150, 450, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 150, 400, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 150, 350, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 150, 300, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 150, 250, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 150, 200, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 150, 150, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 150, 100, 40, 40, DARK_GREEN, DARK_GREEN, None)

    # 3st column of boxes
    button('', 200, 450, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 200, 400, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 200, 350, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 200, 300, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 200, 250, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 200, 200, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 200, 150, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 200, 100, 40, 40, DARK_GREEN, DARK_GREEN, None)

    # 4st column of boxes
    button('', 250, 450, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 250, 400, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 250, 350, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 250, 300, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 250, 250, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 250, 200, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 250, 150, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 250, 100, 40, 40, DARK_GREEN, DARK_GREEN, None)

    # 5st column of boxes
    button('', 300, 450, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 300, 400, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 300, 350, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 300, 300, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 300, 250, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 300, 200, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 300, 150, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 300, 100, 40, 40, DARK_GREEN, DARK_GREEN, None)

    # 6st column of boxes
    button('', 350, 450, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 350, 400, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 350, 350, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 350, 300, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 350, 250, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 350, 200, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 350, 150, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 350, 100, 40, 40, DARK_GREEN, DARK_GREEN, None)

    # 7st column of boxes
    button('', 400, 450, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 400, 400, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 400, 350, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 400, 300, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 400, 250, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 400, 200, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 400, 150, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 400, 100, 40, 40, DARK_GREEN, DARK_GREEN, None)

    # 8st column of boxes
    button('', 450, 450, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 450, 400, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 450, 350, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 450, 300, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 450, 250, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 450, 200, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 450, 150, 40, 40, DARK_GREEN, DARK_GREEN, None)
    button('', 450, 100, 40, 40, DARK_GREEN, DARK_GREEN, None)
    return_text('Press the letter "m" for Main Menu', WHITE)

    # Drawing the score board circles:
    pygame.draw.circle(gameDisplay, WHITE, (530, 170), circle_radius)
    pygame.draw.circle(gameDisplay, BLACK, (530, 120), circle_radius)
    message_display3('OTHELLO', WHITE)
    pygame.display.update()


# Player vs Player Screen
def player_player():
    """This function creates the player vs player screen.
    It allows the players to place the round pieces on the board when a square is clicked.
    Implements the rules of the game."""
    turn = 0
    display_board()
    reset_array(board)
    setting_up_board(board)
    player_score(board)
    pygame.display.update()
    game_exit = False
    while not game_exit:
        mouse = pygame.mouse.get_pos()
        draw_piece_in_display(turn)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    second_display()
                    game_exit = True
            if event.type == pygame.MOUSEBUTTONUP and (100 < mouse[0] < 490 and 100 < mouse[1] < 490):
                if turn == 0:
                    enforce_rules(board, 1)
                else:
                    enforce_rules(board, 2)
                if player_score(board):
                    game_exit = True

                turn += 1
                turn %= 2
            pygame.display.update()


# Player vs Computer Screen
def player_computer():
    """This function creates the player vs computer screen.
    It allows the player and the computer to place the round pieces on the board when a square is clicked.
    Implements the rules of the game."""
    turn = 0
    display_board()
    reset_array(board)
    setting_up_board(board)
    game_exit = False
    while not game_exit:
        draw_piece_in_display(turn)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    second_display()
                    game_exit = True
            if event.type == pygame.MOUSEBUTTONUP:
                enforce_rules(board, 1)  # Will change array
                computer_move(board, 1)  # Computer makes a valid move
                enforce_rules(board, 2)  # Will change the array for the computer
                if player_score(board):
                    game_exit = True

                turn += 1
                turn %= 2
            pygame.display.update()


# Player vs Computer Screen
def computer_computer():
    """This function creates the computer vs computer screen.
    It allows the computer to have two different turns to place the round pieces on the board when a square is clicked.
    Implements the rules of the game."""
    display_board()
    reset_array(board)
    setting_up_board(board)
    game_exit = False
    while not game_exit:
        pygame.time.wait(500)
        # draw_piece_in_display(turn)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    second_display()
                    game_exit = True
        computer_move(board, 0)  # Computer makes a valid move
        enforce_rules(board, 1)  # will change the array for the computer
        computer_move(board, 1)  # Computer makes a valid move
        enforce_rules(board, 2)  # will change the array for the computer
        if player_score(board):
            game_exit = True
        pygame.display.update()


# How to Play Screen
def how_to_play():
    """This function creates the how to play screen. It displays the instructions image in the pygame display. """
    x = 0
    y = 0
    gameDisplay.fill(WHITE)
    directions_image(x, y)
    return_text('Press the letter "m" for Main Menu', BLACK)
    pygame.display.update()
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    second_display()
                    game_exit = True


# New definition
def setting_up_board(board):
    """This function sets up the board given the board.
    It also changes the array so that the game will be able to run properly. """
    board[3][3] = 1
    pygame.draw.circle(gameDisplay, BLACK, (270, 320), circle_radius)
    board[3][4] = 2
    pygame.draw.circle(gameDisplay, WHITE, (320, 320), circle_radius)
    board[4][3] = 2
    pygame.draw.circle(gameDisplay, WHITE, (270, 270), circle_radius)
    board[4][4] = 1
    pygame.draw.circle(gameDisplay, BLACK, (320, 270), circle_radius)
    return board


def computer_move(board, move):
    """This function creates the AI of the game.
    It takes the board of the game and a move for the computer.
    It creates a move using random and returning booleans. """
    while True:
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        if move == 0:
            if board[x][y] == 0:
                board[x][y] = 1
                return False
        elif move == 1:
            if board[x][y] == 0:
                board[x][y] = 2
                return False


def reset_array(array):
    """This function resets the array that resembles the board on pygame to the console.
    It takes an array with the same number of columns and rows of the board and it reset it after each move."""
    for i, e in enumerate(array):
        if isinstance(e, list):
            reset_array(e)
        else:
            array[i] = 0


def score(text, color, posx, posy):
    """This function displays the score of each player.
    Parameters include the text, color, and the x and y coordinate to display the text. """
    largeText = pygame.font.Font('times new roman.ttf', 35)
    TextSurface, TextRectangle = text_objects(text, largeText, color)
    TextRectangle.center = ((posx), (posy))
    gameDisplay.blit(TextSurface, TextRectangle)


# Function to keep track of the scores of each player
def player_score(board):
    """This function keeps track of the score of each player.
    It takes the board to check how many pieces of each color are in the game board and
    compares the scores to return boolean values if player x wins. """
    player1_score = 0
    player2_score = 0
    zeros = 64
    for row in range(rows):
        for column in range(columns):
            if board[row][column] == 1:
                player1_score += 1
                button('', 568, 100, 40, 40, WHITE, WHITE, action=None)
                score(str(player1_score), BLACK, 590, 120)
                zeros -= 1
            elif board[row][column] == 2:
                player2_score += 1
                button('', 568, 150, 40, 40, WHITE, WHITE, action=None)
                score(str(player2_score), BLACK, 590, 170)
                zeros -= 1
            if zeros <= 0:
                if player1_score > player2_score:
                    player_1_win()
                    return True
                elif player1_score < player2_score:
                    player_2_win()
                    return True
                elif player1_score == player2_score:
                    player_tie()
                    return True


def player_1_win():
    """This function creates a screen if player 1 wins.
    It displays a text if the boolean expression from player_score indicates a higher score for the first player. """
    winner_or_tie_text(str(name1), WHITE)


def player_2_win():
    """This function creates a screen if player 2 wins.
    It displays a text if the boolean expression from player_score indicates a higher score for the second player. """
    winner_or_tie_text(str(name2), WHITE)


def player_tie():
    """This function creates a screen if there is a tie.
    It displays a text if the boolean expression from player_score indicates a higher score for the second player. """
    winner_or_tie_text("Tie!", WHITE)


def draw_piece_in_display(move):
    """This function draws the circles over the squares when clicked.
    It takes the location of the click and draws a circle with specifications such as location, color, and size. """
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # First Column
    if click[0] == 1 and (100 + 40 > mouse[0] > 100 and 450 + 40 > mouse[1] > 450) and (board[0][0] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (120, 470), circle_radius)  # Surface, color, position x, radius
        else:
            pygame.draw.circle(gameDisplay, WHITE, (120, 470), circle_radius)
        piece_placed(0, 0, move, board)
    elif click[0] == 1 and (100 + 40 > mouse[0] > 100 and 400 + 40 > mouse[1] > 400) and (board[1][0] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (120, 420), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (120, 420), circle_radius)
        piece_placed(1, 0, move, board)
    elif click[0] == 1 and (100 + 40 > mouse[0] > 100 and 350 + 40 > mouse[1] > 350) and (board[2][0] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (120, 370), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (120, 370), circle_radius)
        piece_placed(2, 0, move, board)
    elif click[0] == 1 and (100 + 40 > mouse[0] > 100 and 300 + 40 > mouse[1] > 300) and (board[3][0] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (120, 320), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (120, 320), circle_radius)
        piece_placed(3, 0, move, board)
    elif click[0] == 1 and (100 + 40 > mouse[0] > 100 and 250 + 40 > mouse[1] > 250) and (board[4][0] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (120, 270), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (120, 270), circle_radius)
        piece_placed(4, 0, move, board)
    elif click[0] == 1 and (100 + 40 > mouse[0] > 100 and 200 + 40 > mouse[1] > 200) and (board[5][0] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (120, 220), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (120, 220), circle_radius)
        piece_placed(5, 0, move, board)
    elif click[0] == 1 and (100 + 40 > mouse[0] > 100 and 150 + 40 > mouse[1] > 150) and (board[6][0] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (120, 170), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (120, 170), circle_radius)
        piece_placed(6, 0, move, board)
    elif click[0] == 1 and (100 + 40 > mouse[0] > 100 and 100 + 40 > mouse[1] > 100) and (board[7][0] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (120, 120), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (120, 120), circle_radius)
        piece_placed(7, 0, move, board)

    # Second Column
    elif click[0] == 1 and (150 + 40 > mouse[0] > 150 and 450 + 40 > mouse[1] > 450) and (board[0][1] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (170, 470), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (170, 470), circle_radius)
        piece_placed(0, 1, move, board)
    elif click[0] == 1 and (150 + 40 > mouse[0] > 150 and 400 + 40 > mouse[1] > 400) and (board[1][1] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (170, 420), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (170, 420), circle_radius)
        piece_placed(1, 1, move, board)
    elif click[0] == 1 and (150 + 40 > mouse[0] > 150 and 350 + 40 > mouse[1] > 350) and (board[2][1] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (170, 370), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (170, 370), circle_radius)
        piece_placed(2, 1, move, board)
    elif click[0] == 1 and (150 + 40 > mouse[0] > 150 and 300 + 40 > mouse[1] > 300) and (board[3][1] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (170, 320), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (170, 320), circle_radius)
        piece_placed(3, 1, move, board)
    elif click[0] == 1 and (150 + 40 > mouse[0] > 150 and 250 + 40 > mouse[1] > 250) and (board[4][1] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (170, 270), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (170, 270), circle_radius)
        piece_placed(4, 1, move, board)
    elif click[0] == 1 and (150 + 40 > mouse[0] > 150 and 200 + 40 > mouse[1] > 200) and (board[5][1] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (170, 220), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (170, 220), circle_radius)
        piece_placed(5, 1, move, board)
    elif click[0] == 1 and (150 + 40 > mouse[0] > 150 and 150 + 40 > mouse[1] > 150) and (board[6][1] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (170, 170), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (170, 170), circle_radius)
        piece_placed(6, 1, move, board)
    elif click[0] == 1 and (150 + 40 > mouse[0] > 150 and 100 + 40 > mouse[1] > 100) and (board[7][1] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (170, 120), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (170, 120), circle_radius)
        piece_placed(7, 1, move, board)

    # Third Column
    elif click[0] == 1 and (200 + 40 > mouse[0] > 200 and 450 + 40 > mouse[1] > 450) and (board[0][2] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (220, 470), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (220, 470), circle_radius)
        piece_placed(0, 2, move, board)
    elif click[0] == 1 and (200 + 40 > mouse[0] > 200 and 400 + 40 > mouse[1] > 400) and (board[1][2] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (220, 420), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (220, 420), circle_radius)
        piece_placed(1, 2, move, board)
    elif click[0] == 1 and (200 + 40 > mouse[0] > 200 and 350 + 40 > mouse[1] > 350) and (board[2][2] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (220, 370), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (220, 370), circle_radius)
        piece_placed(2, 2, move, board)
    elif click[0] == 1 and (200 + 40 > mouse[0] > 200 and 300 + 40 > mouse[1] > 300) and (board[3][2] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (220, 320), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (220, 320), circle_radius)
        piece_placed(3, 2, move, board)
    elif click[0] == 1 and (200 + 40 > mouse[0] > 200 and 250 + 40 > mouse[1] > 250) and (board[4][2] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (220, 270), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (220, 270), circle_radius)
        piece_placed(4, 2, move, board)
    elif click[0] == 1 and (200 + 40 > mouse[0] > 200 and 200 + 40 > mouse[1] > 200) and (board[5][2] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (220, 220), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (220, 220), circle_radius)
        piece_placed(5, 2, move, board)
    elif click[0] == 1 and (200 + 40 > mouse[0] > 200 and 150 + 40 > mouse[1] > 150) and (board[6][2] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (220, 170), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (220, 170), circle_radius)
        piece_placed(6, 2, move, board)
    elif click[0] == 1 and (200 + 40 > mouse[0] > 200 and 100 + 40 > mouse[1] > 100) and (board[7][2] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (220, 120), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (220, 120), circle_radius)
        piece_placed(7, 2, move, board)

    # Fourth Column
    elif click[0] == 1 and (250 + 40 > mouse[0] > 250 and 450 + 40 > mouse[1] > 450) and (board[0][3] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (270, 470), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (270, 470), circle_radius)
        piece_placed(0, 3, move, board)
    elif click[0] == 1 and (250 + 40 > mouse[0] > 250 and 400 + 40 > mouse[1] > 400) and (board[1][3] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (270, 420), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (270, 420), circle_radius)
        piece_placed(1, 3, move, board)
    elif click[0] == 1 and (250 + 40 > mouse[0] > 250 and 350 + 40 > mouse[1] > 350) and (board[2][3] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (270, 370), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (270, 370), circle_radius)
        piece_placed(2, 3, move, board)
    elif click[0] == 1 and (250 + 40 > mouse[0] > 250 and 300 + 40 > mouse[1] > 300) and (board[3][3] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (270, 320), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (270, 320), circle_radius)
        piece_placed(3, 3, move, board)
    elif click[0] == 1 and (250 + 40 > mouse[0] > 250 and 250 + 40 > mouse[1] > 250) and (board[4][3] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (270, 270), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (270, 270), circle_radius)
        piece_placed(4, 3, move, board)
    elif click[0] == 1 and (250 + 40 > mouse[0] > 250 and 200 + 40 > mouse[1] > 200) and (board[5][3] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (270, 220), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (270, 220), circle_radius)
        piece_placed(5, 3, move, board)
    elif click[0] == 1 and (250 + 40 > mouse[0] > 250 and 150 + 40 > mouse[1] > 150) and (board[6][3] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (270, 170), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (270, 170), circle_radius)
        piece_placed(6, 3, move, board)
    elif click[0] == 1 and (250 + 40 > mouse[0] > 250 and 100 + 40 > mouse[1] > 100) and (board[7][3] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (270, 120), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (270, 120), circle_radius)
        piece_placed(7, 3, move, board)

    # Fifth Column
    elif click[0] == 1 and (300 + 40 > mouse[0] > 300 and 450 + 40 > mouse[1] > 450) and (board[0][4] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (320, 470), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (320, 470), circle_radius)
        piece_placed(0, 4, move, board)
    elif click[0] == 1 and (300 + 40 > mouse[0] > 300 and 400 + 40 > mouse[1] > 400) and (board[1][4] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (320, 420), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (320, 420), circle_radius)
        piece_placed(1, 4, move, board)
    elif click[0] == 1 and (300 + 40 > mouse[0] > 300 and 350 + 40 > mouse[1] > 350) and (board[2][4] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (320, 370), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (320, 370), circle_radius)
        piece_placed(2, 4, move, board)
    elif click[0] == 1 and (300 + 40 > mouse[0] > 300 and 300 + 40 > mouse[1] > 300) and (board[3][4] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (320, 320), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (320, 320), circle_radius)
        piece_placed(3, 4, move, board)
    elif click[0] == 1 and (300 + 40 > mouse[0] > 300 and 250 + 40 > mouse[1] > 250) and (board[4][4] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (320, 270), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (320, 270), circle_radius)
        piece_placed(4, 4, move, board)
    elif click[0] == 1 and (300 + 40 > mouse[0] > 300 and 200 + 40 > mouse[1] > 200) and (board[5][4] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (320, 220), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (320, 220), circle_radius)
        piece_placed(5, 4, move, board)
    elif click[0] == 1 and (300 + 40 > mouse[0] > 300 and 150 + 40 > mouse[1] > 150) and (board[6][4] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (320, 170), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (320, 170), circle_radius)
        piece_placed(6, 4, move, board)
    elif click[0] == 1 and (300 + 40 > mouse[0] > 300 and 100 + 40 > mouse[1] > 100) and (board[7][4] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (320, 120), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (320, 120), circle_radius)
        piece_placed(7, 4, move, board)

    # Sixth Column
    elif click[0] == 1 and (350 + 40 > mouse[0] > 350 and 450 + 40 > mouse[1] > 450) and (board[0][5] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (370, 470), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (370, 470), circle_radius)
        piece_placed(0, 5, move, board)
    elif click[0] == 1 and (350 + 40 > mouse[0] > 350 and 400 + 40 > mouse[1] > 400) and (board[1][5] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (370, 420), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (370, 420), circle_radius)
        piece_placed(1, 5, move, board)
    elif click[0] == 1 and (350 + 40 > mouse[0] > 350 and 350 + 40 > mouse[1] > 350) and (board[2][5] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (370, 370), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (370, 370), circle_radius)
        piece_placed(2, 5, move, board)
    elif click[0] == 1 and (350 + 40 > mouse[0] > 350 and 300 + 40 > mouse[1] > 300) and (board[3][5] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (370, 320), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (370, 320), circle_radius)
        piece_placed(3, 5, move, board)
    elif click[0] == 1 and (350 + 40 > mouse[0] > 350 and 250 + 40 > mouse[1] > 250) and (board[4][5] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (370, 270), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (370, 270), circle_radius)
        piece_placed(4, 5, move, board)
    elif click[0] == 1 and (350 + 40 > mouse[0] > 350 and 200 + 40 > mouse[1] > 200) and (board[5][5] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (370, 220), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (370, 220), circle_radius)
        piece_placed(5, 5, move, board)
    elif click[0] == 1 and (350 + 40 > mouse[0] > 350 and 150 + 40 > mouse[1] > 150) and (board[6][5] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (370, 170), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (370, 170), circle_radius)
        piece_placed(6, 5, move, board)
    elif click[0] == 1 and (350 + 40 > mouse[0] > 350 and 100 + 40 > mouse[1] > 100) and (board[7][5] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (370, 120), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (370, 120), circle_radius)
        piece_placed(7, 5, move, board)

    # Seventh Column
    elif click[0] == 1 and (400 + 40 > mouse[0] > 400 and 450 + 40 > mouse[1] > 450) and (board[0][6] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (420, 470), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (420, 470), circle_radius)
        piece_placed(0, 6, move, board)
    elif click[0] == 1 and (400 + 40 > mouse[0] > 400 and 400 + 40 > mouse[1] > 400) and (board[1][6] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (420, 420), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (420, 420), circle_radius)
        piece_placed(1, 6, move, board)
    elif click[0] == 1 and (400 + 40 > mouse[0] > 400 and 350 + 40 > mouse[1] > 350) and (board[2][6] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (420, 370), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (420, 370), circle_radius)
        piece_placed(2, 6, move, board)
    elif click[0] == 1 and (400 + 40 > mouse[0] > 400 and 300 + 40 > mouse[1] > 300) and (board[3][6] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (420, 320), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (420, 320), circle_radius)
        piece_placed(3, 6, move, board)
    elif click[0] == 1 and (400 + 40 > mouse[0] > 400 and 250 + 40 > mouse[1] > 250) and (board[4][6] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (420, 270), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (420, 270), circle_radius)
        piece_placed(4, 6, move, board)
    elif click[0] == 1 and (400 + 40 > mouse[0] > 400 and 200 + 40 > mouse[1] > 200) and (board[5][6] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (420, 220), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (420, 220), circle_radius)
        piece_placed(5, 6, move, board)
    elif click[0] == 1 and (400 + 40 > mouse[0] > 400 and 150 + 40 > mouse[1] > 150) and (board[6][6] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (420, 170), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (420, 170), circle_radius)
        piece_placed(6, 6, move, board)
    elif click[0] == 1 and (400 + 40 > mouse[0] > 400 and 100 + 40 > mouse[1] > 100) and (board[7][6] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (420, 120), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (420, 120), circle_radius)
        piece_placed(7, 6, move, board)

    # Eight Column
    elif click[0] == 1 and (450 + 40 > mouse[0] > 450 and 450 + 40 > mouse[1] > 450) and (board[0][7] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (470, 470), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (470, 470), circle_radius)
        piece_placed(0, 7, move, board)
    elif click[0] == 1 and (450 + 40 > mouse[0] > 450 and 400 + 40 > mouse[1] > 400) and (board[1][7] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (470, 420), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (470, 420), circle_radius)
        piece_placed(1, 7, move, board)
    elif click[0] == 1 and (450 + 40 > mouse[0] > 450 and 350 + 40 > mouse[1] > 350) and (board[2][7] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (470, 370), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (470, 370), circle_radius)
        piece_placed(2, 7, move, board)
    elif click[0] == 1 and (450 + 40 > mouse[0] > 450 and 300 + 40 > mouse[1] > 300) and (board[3][7] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (470, 320), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (470, 320), circle_radius)
        piece_placed(3, 7, move, board)
    elif click[0] == 1 and (450 + 40 > mouse[0] > 450 and 250 + 40 > mouse[1] > 250) and (board[4][7] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (470, 270), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (470, 270), circle_radius)
        piece_placed(4, 7, move, board)
    elif click[0] == 1 and (450 + 40 > mouse[0] > 450 and 200 + 40 > mouse[1] > 200) and (board[5][7] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (470, 220), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (470, 220), circle_radius)
        piece_placed(5, 7, move, board)
    elif click[0] == 1 and (450 + 40 > mouse[0] > 450 and 150 + 40 > mouse[1] > 150) and (board[6][7] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (470, 170), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (470, 170), circle_radius)
        piece_placed(6, 7, move, board)
    elif click[0] == 1 and (450 + 40 > mouse[0] > 450 and 100 + 40 > mouse[1] > 100) and (board[7][7] == 0):
        if move == 0:
            pygame.draw.circle(gameDisplay, BLACK, (470, 120), circle_radius)
        else:
            pygame.draw.circle(gameDisplay, WHITE, (470, 120), circle_radius)
        piece_placed(7, 7, move, board)
    pygame.display.update()


def draw_flipped_piece(board, move):
    """This function draws circles on top of other circles to change the color based on the rules of the game.
    It takes the game board and the move that converts the color of the pieces.
    It displays new circles of the same color if the rules of the game are met."""

    if move == 1:

        # First Row
        if board[0][0] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (120, 470), circle_radius)  # Surface, color, position x, radius
        if board[0][1] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (170, 470), circle_radius)  # Surface, color, position x, radius
        if board[0][2] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (220, 470), circle_radius)
        if board[0][3] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (270, 470), circle_radius)
        if board[0][4] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (320, 470), circle_radius)
        if board[0][5] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (370, 470), circle_radius)
        if board[0][6] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (420, 470), circle_radius)
        if board[0][7] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (470, 470), circle_radius)

        # Second Row
        if board[1][0] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (120, 420), circle_radius)  # Surface, color, position x, radius
        if board[1][1] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (170, 420), circle_radius)  # Surface, color, position x, radius
        if board[1][2] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (220, 420), circle_radius)
        if board[1][3] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (270, 420), circle_radius)
        if board[1][4] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (320, 420), circle_radius)
        if board[1][5] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (370, 420), circle_radius)
        if board[1][6] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (420, 420), circle_radius)
        if board[1][7] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (470, 420), circle_radius)

        # Third Row
        if board[2][0] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (120, 370), circle_radius)  # Surface, color, position x, radius
        if board[2][1] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (170, 370), circle_radius)  # Surface, color, position x, radius
        if board[2][2] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (220, 370), circle_radius)
        if board[2][3] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (270, 370), circle_radius)
        if board[2][4] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (320, 370), circle_radius)
        if board[2][5] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (370, 370), circle_radius)
        if board[2][6] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (420, 370), circle_radius)
        if board[2][7] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (470, 370), circle_radius)

        # Fourth Row
        if board[3][0] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (120, 320), circle_radius)  # Surface, color, position x, radius
        if board[3][1] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (170, 320), circle_radius)  # Surface, color, position x, radius
        if board[3][2] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (220, 320), circle_radius)
        if board[3][3] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (270, 320), circle_radius)
        if board[3][4] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (320, 320), circle_radius)
        if board[3][5] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (370, 320), circle_radius)
        if board[3][6] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (420, 320), circle_radius)
        if board[3][7] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (470, 320), circle_radius)

        # Fifth Row
        if board[4][0] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (120, 270), circle_radius)  # Surface, color, position x, radius
        if board[4][1] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (170, 270), circle_radius)  # Surface, color, position x, radius
        if board[4][2] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (220, 270), circle_radius)
        if board[4][3] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (270, 270), circle_radius)
        if board[4][4] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (320, 270), circle_radius)
        if board[4][5] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (370, 270), circle_radius)
        if board[4][6] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (420, 270), circle_radius)
        if board[4][7] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (470, 270), circle_radius)

        # Sixth Row
        if board[5][0] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (120, 220), circle_radius)  # Surface, color, position x, radius
        if board[5][1] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (170, 220), circle_radius)  # Surface, color, position x, radius
        if board[5][2] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (220, 220), circle_radius)
        if board[5][3] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (270, 220), circle_radius)
        if board[5][4] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (320, 220), circle_radius)
        if board[5][5] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (370, 220), circle_radius)
        if board[5][6] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (420, 220), circle_radius)
        if board[5][7] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (470, 220), circle_radius)

        # Seventh Row
        if board[6][0] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (120, 170), circle_radius)  # Surface, color, position x, radius
        if board[6][1] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (170, 170), circle_radius)  # Surface, color, position x, radius
        if board[6][2] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (220, 170), circle_radius)
        if board[6][3] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (270, 170), circle_radius)
        if board[6][4] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (320, 170), circle_radius)
        if board[6][5] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (370, 170), circle_radius)
        if board[6][6] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (420, 170), circle_radius)
        if board[6][7] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (470, 170), circle_radius)

        # Eight Row
        if board[7][0] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (120, 120), circle_radius)  # Surface, color, position x, radius
        if board[7][1] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (170, 120), circle_radius)  # Surface, color, position x, radius
        if board[7][2] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (220, 120), circle_radius)
        if board[7][3] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (270, 120), circle_radius)
        if board[7][4] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (320, 120), circle_radius)
        if board[7][5] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (370, 120), circle_radius)
        if board[7][6] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (420, 120), circle_radius)
        if board[7][7] == 1:
            pygame.draw.circle(gameDisplay, BLACK, (470, 120), circle_radius)

    else:

        # First Row
        if board[0][0] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (120, 470), circle_radius)  # Surface, color, position x, radius
        if board[0][1] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (170, 470), circle_radius)  # Surface, color, position x, radius
        if board[0][2] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (220, 470), circle_radius)
        if board[0][3] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (270, 470), circle_radius)
        if board[0][4] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (320, 470), circle_radius)
        if board[0][5] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (370, 470), circle_radius)
        if board[0][6] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (420, 470), circle_radius)
        if board[0][7] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (470, 470), circle_radius)

        # Second Row
        if board[1][0] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (120, 420), circle_radius)  # Surface, color, position x, radius
        if board[1][1] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (170, 420), circle_radius)  # Surface, color, position x, radius
        if board[1][2] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (220, 420), circle_radius)
        if board[1][3] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (270, 420), circle_radius)
        if board[1][4] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (320, 420), circle_radius)
        if board[1][5] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (370, 420), circle_radius)
        if board[1][6] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (420, 420), circle_radius)
        if board[1][7] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (470, 420), circle_radius)

        # Third Row
        if board[2][0] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (120, 370), circle_radius)  # Surface, color, position x, radius
        if board[2][1] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (170, 370), circle_radius)  # Surface, color, position x, radius
        if board[2][2] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (220, 370), circle_radius)
        if board[2][3] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (270, 370), circle_radius)
        if board[2][4] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (320, 370), circle_radius)
        if board[2][5] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (370, 370), circle_radius)
        if board[2][6] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (420, 370), circle_radius)
        if board[2][7] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (470, 370), circle_radius)

        # Fourth Row
        if board[3][0] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (120, 320), circle_radius)  # Surface, color, position x, radius
        if board[3][1] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (170, 320), circle_radius)  # Surface, color, position x, radius
        if board[3][2] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (220, 320), circle_radius)
        if board[3][3] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (270, 320), circle_radius)
        if board[3][4] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (320, 320), circle_radius)
        if board[3][5] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (370, 320), circle_radius)
        if board[3][6] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (420, 320), circle_radius)
        if board[3][7] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (470, 320), circle_radius)

        # Fifth Row
        if board[4][0] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (120, 270), circle_radius)  # Surface, color, position x, radius
        if board[4][1] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (170, 270), circle_radius)  # Surface, color, position x, radius
        if board[4][2] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (220, 270), circle_radius)
        if board[4][3] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (270, 270), circle_radius)
        if board[4][4] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (320, 270), circle_radius)
        if board[4][5] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (370, 270), circle_radius)
        if board[4][6] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (420, 270), circle_radius)
        if board[4][7] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (470, 270), circle_radius)

        # Sixth Row
        if board[5][0] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (120, 220), circle_radius)  # Surface, color, position x, radius
        if board[5][1] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (170, 220), circle_radius)  # Surface, color, position x, radius
        if board[5][2] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (220, 220), circle_radius)
        if board[5][3] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (270, 220), circle_radius)
        if board[5][4] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (320, 220), circle_radius)
        if board[5][5] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (370, 220), circle_radius)
        if board[5][6] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (420, 220), circle_radius)
        if board[5][7] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (470, 220), circle_radius)

        # Seventh Row
        if board[6][0] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (120, 170), circle_radius)  # Surface, color, position x, radius
        if board[6][1] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (170, 170), circle_radius)  # Surface, color, position x, radius
        if board[6][2] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (220, 170), circle_radius)
        if board[6][3] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (270, 170), circle_radius)
        if board[6][4] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (320, 170), circle_radius)
        if board[6][5] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (370, 170), circle_radius)
        if board[6][6] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (420, 170), circle_radius)
        if board[6][7] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (470, 170), circle_radius)

        # Eight Row
        if board[7][0] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (120, 120), circle_radius)  # Surface, color, position x, radius
        if board[7][1] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (170, 120), circle_radius)  # Surface, color, position x, radius
        if board[7][2] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (220, 120), circle_radius)
        if board[7][3] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (270, 120), circle_radius)
        if board[7][4] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (320, 120), circle_radius)
        if board[7][5] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (370, 120), circle_radius)
        if board[7][6] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (420, 120), circle_radius)
        if board[7][7] == 2:
            pygame.draw.circle(gameDisplay, WHITE, (470, 120), circle_radius)

    pygame.display.update()


# This is what changes the matrix
def enforce_rules(board, move):
    """This function changes the matrix that resembles the game board.
    It takes the board and the last move, which is based on numbers 0 and 1, and
    updates the matrix on the console with the new moves. """

    # Check for horizontal locations for pieces to be flipped
    for row in range(rows):
        for column in range(columns - 2):
            if board[row][column] == move and board[row][column + 1] != 0 and board[row][column + 2] == move:
                board[row][column] = move
                board[row][column + 1] = move
                board[row][column + 2] = move
                draw_flipped_piece(board, move)

    for row in range(rows):
        for column in range(columns - 3):
            if board[row][column] == move and board[row][column + 1] != 0 and board[row][column + 2] != 0 and board[row][column + 3] == move:
                board[row][column] = move
                board[row][column + 1] = move
                board[row][column + 2] = move
                board[row][column + 3] = move
                draw_flipped_piece(board, move)

    for row in range(rows):
        for column in range(columns - 4):
            if board[row][column] == move and board[row][column + 1] != 0 and board[row][column + 2] != 0 and board[row][column + 3] != 0 and board[row][column + 4] == move:
                board[row][column] = move
                board[row][column + 1] = move
                board[row][column + 2] = move
                board[row][column + 3] = move
                board[row][column + 4] = move
                draw_flipped_piece(board, move)

    for row in range(rows):
        for column in range(columns - 5):
            if board[row][column] == move and board[row][column + 1] != 0 and board[row][column + 2] != 0 and board[row][column + 3] != 0 and board[row][column + 4] == move and board[row][column + 5] == move:
                board[row][column] = move
                board[row][column + 1] = move
                board[row][column + 2] = move
                board[row][column + 3] = move
                board[row][column + 4] = move
                board[row][column + 5] = move
                draw_flipped_piece(board, move)

    for row in range(rows):
        for column in range(columns - 6):
            if board[row][column] == move and board[row][column + 1] != 0 and board[row][column + 2] != 0 and board[row][column + 3] != 0 and board[row][column + 4] == move and board[row][column + 5] == move and board[row][column + 6] == move:
                board[row][column] = move
                board[row][column + 1] = move
                board[row][column + 2] = move
                board[row][column + 3] = move
                board[row][column + 4] = move
                board[row][column + 5] = move
                board[row][column + 6] = move
                draw_flipped_piece(board, move)

    for row in range(rows):
        for column in range(columns - 7):
            if board[row][column] == move and board[row][column + 1] != 0 and board[row][column + 2] != 0 and board[row][column + 3] != 0 and board[row][column + 4] == move and board[row][column + 5] == move and board[row][column + 6] == move and board[row][column + 7] == move:
                board[row][column] = move
                board[row][column + 1] = move
                board[row][column + 2] = move
                board[row][column + 3] = move
                board[row][column + 4] = move
                board[row][column + 5] = move
                board[row][column + 6] = move
                board[row][column + 7] = move
                draw_flipped_piece(board, move)

    # Check for vertical locations for pieces to be flipped
    for row in range(rows - 2):
        for column in range(columns):
            if board[row][column] == move and board[row + 1][column] != 0 and board[row + 2][column] == move:
                board[row][column] = move
                board[row + 1][column] = move
                board[row + 2][column] = move
                draw_flipped_piece(board, move)

    for row in range(rows - 3):
        for column in range(columns):
            if board[row][column] == move and board[row + 1][column] != 0 and board[row + 2][column] != 0 and board[row + 3][column] == move:
                board[row][column] = move
                board[row + 1][column] = move
                board[row + 2][column] = move
                board[row + 3][column] = move
                draw_flipped_piece(board, move)

    for row in range(rows - 4):
        for column in range(columns):
            if board[row][column] == move and board[row + 1][column] != 0 and board[row + 2][column] != 0 and board[row + 3][column] != 0 and board[row + 4][column] == move:
                board[row][column] = move
                board[row + 1][column] = move
                board[row + 2][column] = move
                board[row + 3][column] = move
                board[row + 4][column] = move
                draw_flipped_piece(board, move)

    for row in range(rows - 5):
        for column in range(columns):
            if board[row][column] == move and board[row + 1][column] != 0 and board[row + 2][column] != 0 and board[row + 3][column] != 0 and board[row + 4][column] == move and board[row + 5][column] == move:
                board[row][column] = move
                board[row + 1][column] = move
                board[row + 2][column] = move
                board[row + 3][column] = move
                board[row + 4][column] = move
                board[row + 5][column] = move
                draw_flipped_piece(board, move)

    for row in range(rows - 6):
        for column in range(columns):
            if board[row][column] == move and board[row + 1][column] != 0 and board[row + 2][column] != 0 and board[row + 3][column] != 0 and board[row + 4][column] == move and board[row + 5][column] == move and board[row + 6][column] == move:
                board[row][column] = move
                board[row + 1][column] = move
                board[row + 2][column] = move
                board[row + 3][column] = move
                board[row + 4][column] = move
                board[row + 5][column] = move
                board[row + 6][column] = move
                draw_flipped_piece(board, move)

    for row in range(rows - 7):
        for column in range(columns):
            if board[row][column] == move and board[row + 1][column] != 0 and board[row + 2][column] != 0 and board[row + 3][column] != 0 and board[row + 4][column] == move and board[row + 5][column] == move and board[row + 6][column] != 0 and board[row + 7][column] == move:
                board[row][column] = move
                board[row + 1][column] = move
                board[row + 2][column] = move
                board[row + 3][column] = move
                board[row + 4][column] = move
                board[row + 5][column] = move
                board[row + 6][column] = move
                board[row + 7][column] = move
                draw_flipped_piece(board, move)

    # Check for positive diagonal locations for pieces to be flipped
    for row in range(rows - 2):
        for column in range(columns - 2):
            if board[row][column] == move and board[row + 1][column + 1] != 0 and board[row + 2][column + 2] == move:
                board[row][column] = move
                board[row + 1][column + 1] = move
                board[row + 2][column + 2] = move
                draw_flipped_piece(board, move)

    for row in range(rows - 3):
        for column in range(columns - 3):
            if board[row][column] == move and board[row + 1][column + 1] != 0 and board[row + 2][column + 2] != 0 and board[row + 3][column + 3] == move:
                board[row][column] = move
                board[row + 1][column + 1] = move
                board[row + 2][column + 2] = move
                board[row + 3][column + 3] = move
                draw_flipped_piece(board, move)

    for row in range(rows - 4):
        for column in range(columns - 4):
            if board[row][column] == move and board[row + 1][column + 1] != 0 and board[row + 2][column + 2] != 0 and board[row + 3][column + 3] != 0 and board[row + 4][column + 4] == move:
                board[row][column] = move
                board[row + 1][column + 1] = move
                board[row + 2][column + 2] = move
                board[row + 3][column + 3] = move
                board[row + 4][column + 4] = move
                draw_flipped_piece(board, move)

    for row in range(rows - 5):
        for column in range(columns - 5):
            if board[row][column] == move and board[row + 1][column + 1] != 0 and board[row + 2][column + 2] != 0 and board[row + 3][column + 3] != 0 and board[row + 4][column + 4] != 0 and board[row + 5][column + 5] == move:
                board[row][column] = move
                board[row + 1][column + 1] = move
                board[row + 2][column + 2] = move
                board[row + 3][column + 3] = move
                board[row + 4][column + 4] = move
                board[row + 5][column + 5] = move
                draw_flipped_piece(board, move)

    for row in range(rows - 6):
        for column in range(columns - 6):
            if board[row][column] == move and board[row + 1][column + 1] != 0 and board[row + 2][column + 2] != 0 and board[row + 3][column + 3] != 0 and board[row + 4][column + 4] != 0 and board[row + 5][column + 5] != 0 and board[row + 6][column + 6] == move:
                board[row][column] = move
                board[row + 1][column + 1] = move
                board[row + 2][column + 2] = move
                board[row + 3][column + 3] = move
                board[row + 4][column + 4] = move
                board[row + 5][column + 5] = move
                board[row + 6][column + 6] = move
                draw_flipped_piece(board, move)

    for row in range(rows - 7):
        for column in range(columns - 7):
            if board[row][column] == move and board[row + 1][column + 1] != 0 and board[row + 2][column + 2] != 0 and board[row + 3][column + 3] != 0 and board[row + 4][column + 4] != 0 and board[row + 5][column + 5] != 0and board[row + 6][column + 6] != 0 and board[row + 7][column + 7] == move:
                board[row][column] = move
                board[row + 1][column + 1] = move
                board[row + 2][column + 2] = move
                board[row + 3][column + 3] = move
                board[row + 4][column + 4] = move
                board[row + 5][column + 5] = move
                board[row + 6][column + 6] = move
                board[row + 7][column + 7] = move
                draw_flipped_piece(board, move)

    # Check for negatively diagonal locations for pieces to be flipped
    for row in range(2, rows):
        for column in range(columns - 2):
            if board[row][column] == move and board[row - 1][column + 1] != 0 and board[row - 2][column + 2] == move:
                board[row][column] = move
                board[row - 1][column + 1] = move
                board[row - 2][column + 2] = move
                draw_flipped_piece(board, move)

    for row in range(3, rows):
        for column in range(columns - 3):
            if board[row][column] == move and board[row - 1][column + 1] != 0 and board[row - 2][column + 2] != 0 and board[row - 3][column + 3] == move:
                board[row][column] = move
                board[row - 1][column + 1] = move
                board[row - 2][column + 2] = move
                board[row - 3][column + 3] = move
                draw_flipped_piece(board, move)

    for row in range(4, rows):
        for column in range(columns - 4):
            if board[row][column] == move and board[row - 1][column + 1] != 0 and board[row - 2][column + 2] != 0 and board[row - 3][column + 3] != 0 and board[row - 4][column + 4] == move:
                board[row][column] = move
                board[row - 1][column + 1] = move
                board[row - 2][column + 2] = move
                board[row - 3][column + 3] = move
                board[row - 4][column + 4] = move
                draw_flipped_piece(board, move)

    for row in range(5, rows):
        for column in range(columns - 5):
            if board[row][column] == move and board[row - 1][column + 1] != 0 and board[row - 2][column + 2] != 0 and board[row - 3][column + 3] != 0 and board[row - 4][column + 4] != 0 and board[row - 5][column + 5] == move:
                board[row][column] = move
                board[row - 1][column + 1] = move
                board[row - 2][column + 2] = move
                board[row - 3][column + 3] = move
                board[row - 4][column + 4] = move
                board[row - 5][column + 5] = move
                draw_flipped_piece(board, move)

    for row in range(6, rows):
        for column in range(columns - 6):
            if board[row][column] == move and board[row - 1][column + 1] != 0 and board[row - 2][column + 2] != 0 and board[row - 3][column + 3] != 0 and board[row - 4][column + 4] != 0 and board[row - 5][column + 5] != 0 and board[row - 6][column + 6] == move:
                board[row][column] = move
                board[row - 1][column + 1] = move
                board[row - 2][column + 2] = move
                board[row - 3][column + 3] = move
                board[row - 4][column + 4] = move
                board[row - 5][column + 5] = move
                board[row - 6][column + 6] = move
                draw_flipped_piece(board, move)

    for row in range(7, rows):
        for column in range(columns - 7):
            if board[row][column] == move and board[row - 1][column + 1] != 0 and board[row - 2][column + 2] != 0 and board[row - 3][column + 3] != 0 and board[row - 4][column + 4] != 0 and board[row - 5][column + 5] != 0 and board[row - 6][column + 6] != 0 and board[row - 7][column + 7] == move:
                board[row][column] = move
                board[row - 1][column + 1] = move
                board[row - 2][column + 2] = move
                board[row - 3][column + 3] = move
                board[row - 4][column + 4] = move
                board[row - 5][column + 5] = move
                board[row - 6][column + 6] = move
                board[row - 7][column + 7] = move
                draw_flipped_piece(board, move)


# Ending the game function
def quit_game():
    """This function quits pygame."""
    pygame.quit()
    quit()

# Calling the game intro to begin the game
game_intro()

