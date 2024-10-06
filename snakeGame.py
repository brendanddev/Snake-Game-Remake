# This is an imitation of the classic 2D game 'Snake' which has been developed using Python 
# & the 'PyGame' framework. 

# Developed by Brendan D, June 10th 2024.

# All rights due to Taneli Armanto, Snake's creator. **** THIS WAS MEANT TO BE A PROJECT TO SEE IF I COULD REPLICATE IT USING PYTHON ****

# Library Imports
import pygame # Imports 'pygame' framework
import time # Imports time module
import random # Imports random module to generate random numbers

# Initializing the 'pygame' module from the framework
pygame.init() 

# Defining width and height of the graphics application/display dimensions
info_height = 50 
game_display_width = 400 # Width set to 400 pixels
game_display_height = 400 # Height set to 400 pixels

# Defining variables responsible for the colors
black_color = (0, 0, 0) # Color for text
yellow_color = (161, 240, 0) # Color for snake body
blue_color = (161, 240, 255) # Color for background
red_color = (211, 1, 96) # Color for snake food
pink_color = (168, 50, 149) # Color for super snake food

# Creating and initializing the graphics application/display window

# The variable 'dis' is assigned to the 'pygame'  display module which allows for the
# graphical application to work in python. The function/method 'set_mode' takes the two 
# variables 'display_width' and 'display_height' as arguments which is setting the width
# and height of the display in pixels.
game_display = pygame.display.set_mode((game_display_width, game_display_height + info_height)) 
# The 'pygame's display sets the title/caption of the window to the string 'Replica Snake Game'
# using the 'set_caption' method/function.
pygame.display.set_caption('Replica Snake Game')

# Initiazlizing time, speed, and size variables
game_clock = pygame.time.Clock() # Initializes a variable 'clock' which holds the 'pygame's time module
snake_block = 10 # Initializes and assigns 10 to the 'snake_block' variable representing the size of each block
snake_speed = 20 # Initializes and assings 15 to the 'snake_speed' variable which represents how many pixels the snake will move by

# Initializing font 
font_type = pygame.font.SysFont(None, 20) # The variable 'font_style' is assigned to a font 'None' meaning it will use the default 'pygame' font
                                           # The size of the font is set to 50 pixels


# Function responsible for drawing the 'snake'
def the_snake_display(snake_block, snake_list): # The function takes 'snake_block' and 'snake_list' as arguments
    for x in snake_list: # This loop iterates over each part of the 'snake' which is stored in 'snake_list',
                         # where 'x' is responsible for each of the 'snake's coordinates
        pygame.draw.rect(game_display, yellow_color, [x[0], x[1], snake_block, snake_block]) # The 'draw' method from the 'pygame' library draws the 'snake' as a rectangle
                                                                             # on the game display 'dis', where each drawing will be black, at a specified
                                                                             # postision based on the 'x' and 'y' coordinates of the current part. Where 
                                                                             # the width and height rely on the 'snake_block' variable for dimensions

# Function responsible for displaying a message to the user on the game display
def message(msg, color): # The function takes 'msg' and 'color' as arguments
    mesg = font_type.render(msg, True, color) # The variable 'mseg' creates the text in the font assigned to 'font_style'
                                               # 'True' represents the fact the anti aliasing is enabled
                                               # 'color' holds the color that the text will be
    game_display.blit(mesg, [game_display_width / 6, game_display_height / 3 + info_height]) # 'blit' will draw the text created onto the game display 'dis' where the text is assigned to 'mseg',
                                                            # and the location of the text is dependent on the width and height of the game display

# Function responsible for displaying a menu message on the game display
def menu_message(msg, color, y_pos): # The function takes three parameters, 'msg', 'color', and 'y_pos'
    # The variable 'meu_msg' uses the 'render' method with the 'font_type' object to render the text on a surface
    menu_msg = font_type.render(msg, True, color)
    # The variable 'text' is assigned to the 'get_rect' method responsible for retreiving the area of the surface of the rendered text in the form of a rectangle.
    text = menu_msg.get_rect(center=(game_display_width / 2, y_pos))
    # In order to draw the text at the desired postision of the game display, the 'blit' method is used on the 'game_display' variable,
    # to draw (blit) the text on the text surface which is saved in 'menu_msg', where the postision is relying on the 'text.top_left'
    game_display.blit(menu_msg, text.topleft)

# This function is responsible for the Snake Game Remake's Menu. It will consist of text that will prompt the user in choosing the difficulty
# of the game.
def game_menu():
    # The global variable 'snake_speed' is responsible for controlling how fast the snake will move across the screen.
    # The variable is declared as it will be manipulated and updated depending on the game difficulty chosen by the user.
    global snake_speed
    # The display 'game_display' is coloured to be the color blue 'blue_color' by using the 'fill' method to fill the screen with the specified color.
    game_display.fill(blue_color)
    # By calling the 'menu_message' function, each of the following lines are used to display the text on the screen, each of which at different 'y' levels.
    menu_message("Welcome to Snake, the replica version developed by Drendos!", black_color, 100)
    menu_message("All rights reserved to Taneli Armanto", black_color, 150)
    menu_message("Choose your difficulty:", black_color, 200)
    menu_message("Press 'E' for Easy Difficulty", black_color, 220)
    menu_message("Press 'M' for Medium Difficulty", black_color, 240)
    menu_message("Press 'H' for Hard Difficulty", black_color, 260)
    # The 'pygame' display is updated so that the text is rendered on the display by calling the 'update' method.
    pygame.display.update()

    # A variable 'y_pos' is declared and initialized to the height of the game display divided by 3.
    y_pos = game_display_height / 3

    # This infinite while loop is responsible for changing the speed of the snake depending on which difficulty the user has chosen.
    while True:
        # This for loop checks all 'events' that are in the queue of the 'pygame'.
        for event in pygame.event.get():
            # This outer if statement checks if the user has pressed down on a key as an 'event'.
            if event.type == pygame.KEYDOWN:
                # This inner if statement checks if the user has pressed the 'e' key which indicates they have chosen the easy difficulty.
                if event.key == pygame.K_e:
                    # If they have chosen the easy difficulty, the speed of the snake 'snake_speed' is set to 15.
                    snake_speed = 15
                    # The loop is exited with the 'return' statement
                    return
                # The Else If statement checks if the key the user has pressed is 'm' indicating the medium difficulty.
                elif event.key == pygame.K_m:
                    # If this is the case, the speed of the snake 'snake_speed' is set to 20.
                    snake_speed = 20
                    # The return statement is used to exit the loop.
                    return
                # This Else If statement checks if the key the user has pressed is 'h', which indicates that they have chosen the hard difficulty.
                elif event.key == pygame.K_h:
                    # If this is the case, the speed of the snake 'snake_speed' is set to 30.
                    snake_speed = 30
                    # The return statement is used to exit the loop.
                    return
        # The 'y_pos' variable is incremented by 20, and the games display 'pygame.display' is updated using the 'update' method.
        y_pos = y_pos + 20
        pygame.display.update()


# Function responsible for the game loop which relies on the 'pygame' library, this is the main function of the game.
# This function consists of majority of the logic that controls the flow of the Snake Game Remake.
def main_game_loop():
    # A variable 'score' is declared and initialized to 0. This will track the score of the game.
    score = 0
    # A variable 'high_score' is declared and initialized to 0. This will track the high score of the game.
    high_score = 0
    # The 'start_time' variable will store the time at which the game has started. It uses the 'time' function from the time module, and returns a decimal value
    # which represents the current time at which the game was started. This will be used to track the time of the game.
    start_time = time.time()
    
    # The variable 'game_over' is responsible for the end of the game. This variable will be set to True if the game has ended.
    game_over = False
    # The variable 'game_close' is responsible for the state of the game. It is responsible for any instance where the game is about to restart, or closed.  
    game_close = False

    # The variables 'x1' and 'y1' are responsible for the beggining postision of the snakes 'head' on the game display.

    # The variable 'x1' holds a random integer between 0 and the width of the game display 'game_display_width' minus the width of the snake block itself 'snake_block'.
    # The random number is generated using the 'random.randrange(...)' function from the random module. The purpose is so that the snakes head appears at a randomly generated
    # postision, and that it does not exceed the width of the games display. The random value generated is rounded using the 'round' function, where the value is aligned in a grid
    # like manner by dividing and multiplying the random value by 10.
    x1 = round(random.randrange(0, game_display_width - snake_block) / 10.0) * 10.0

    # The variable 'y1' holds a random integer that is between 0 and the height of the game display 'game_display_height', but factoring in the menu at the top of the game screen,
    # in addition to the height of the blocks of the snake. The 'info_height' variable is responsible for the section of the game screen that provides the user with some game information,
    # like the score, high score, and time of their game. The random value generated is rounded using the 'round' function, where the value is aligned in a grid like manner by dividing and
    #  multiplying the random value by 10.
    y1 = round(random.randrange(info_height, game_display_height - snake_block) / 10.0) * 10.0

    # The variable 'x1_direction_change' is responsible for the control of the snakes direction along the 'x' axis of the game screen.
    # This will manipulate the direction of the snake horizontally (width).
    x1_direction_change = 0
    # The variable 'y1_direction_change' is responsible for the control of the snakes direction along the 'y' axis of the games screen.
    # This will manipulate the direction of the snake vertically (height).
    y1_direction_change = 0

    # The variable 'snake_List' is currently an empty list, but is responsible for storing each of the postisions and parts of the snakes body.
    snake_List = []
    # The beggining of the game the snake starts with just its 'head', which is why the variable 'Length_of_snake' is currently 1.
    Length_of_snake = 1

    # The 'food_x' and 'food_y' variables are responsible for the postisions of the basic snake food of the game.

    # The variable 'food_x' uses the 'randrange' method from the 'random' module to generate a random postision for the food along the 'x' axis of the game.
    # The value is rounded, and divided then multiplied so the food appears in a grid like manner.
    food_x = round(random.randrange(0, game_display_width - snake_block) / 10.0) * 10.0

    # The variable 'food_y' uses the 'randrange' method from the 'random' module aswell, like the 'x' postision, this is used to generate a random postision for
    # the food along the 'y' axis of the game screen. This value is rounded and multiplied, then divided aswell so the food appears in a grid like manner.
    food_y = round(random.randrange(info_height, game_display_height - snake_block) / 10.0) * 10.0

    # The variables 'super_food_x' and 'super_food_y' are responsible for the postisions of the super food in the snake game.

     # The variable 'super_food_x' uses the 'randrange' method from the 'random' module to generate a random postision for the super food along the 'x' axis 
     # of the game. The value is rounded, and divided then multiplied so the super food appears in a grid like manner.
    super_food_x = round(random.randrange(0, game_display_width - snake_block) / 10.0) * 10.0

    # The variable 'super_food_y' uses the 'randrange' method from the 'random' module aswell, like the 'x' postision, this is used to generate a random 
    # postision for the food along the 'y' axis of the game screen. This value is rounded and multiplied, then divided aswell so the food appears in a grid
    # like manner.
    super_food_y = round(random.randrange(info_height, game_display_height - snake_block) / 10.0) * 10.0

    dodge_x = 1
    dodge_y = 1

    # Calls the 'game_menu' function so the games menu appears.
    game_menu()

    # This while loop will continue to execute as long as the game is not over, as 'game_over' currently holds false.
    while not game_over:

        # The variable 'game_time' holds the amount of time since the game started.
        game_time = time.time() - start_time
        # The variable 'game_minutes' converts the games elapsed time to minutes.
        game_minutes = int(game_time // 60)
        # The variable 'game_seconds' converts the games elapsed time into seconds.
        game_seconds = int(game_time % 60)

        # The variable 'timer_text holds the time, and formats the games time into a format of 'MINUTES:SECONDS'.
        timer_text = "Time: {:02d}:{:02d}".format(game_minutes, game_seconds)
        # The variable 'timer_font' holds the font that will be used for the games timer.
        timer_font = pygame.font.SysFont(None, 25)
        #'timer_surface' renders the timer text onto a surface.
        timer_surface = timer_font.render(timer_text, True, black_color)
        
        # This if statement is responsible for updating the games high score, if the current score is larger than the high score,
        # a new high score has been achieved.
        if score > high_score:
            # The value of the 'high_score' variable is reassigned to the contents of the 'score' variable.
            high_score = score

          # The variable 'high_score_text holds the games high score 'high_score' formatted.
        high_score_text = "High Score: {}".format(high_score)
         #'high_score_surface' renders the high score onto a surface.
        high_score_surface = timer_font.render(high_score_text, True, black_color)

        # This for loop is responsible for iterating over each event retreived using the 'event.get' from the 'pygame' framework.
        for event in pygame.event.get():
            # This if statement checks if the type of event was 'QUIT', which causes the game to end.
            if event.type == pygame.QUIT:
                # The 'game_over' variable is now true.
                game_over = True
            # This if statement checks if the type of event was a user pressing a key, which indicates that the user has moved the snake.
            if event.type == pygame.KEYDOWN:
                # This inner if statement checks if the user has pressed down on the left arrow key.
                if event.key == pygame.K_LEFT:
                    # If this is the case, the snakes direction will be changed. The snake will now move left by one block size which is done
                    # by making the value of 'snake_block' negative.
                    x1_direction_change = -snake_block
                    # The vertical direction will not be changed as the left arrow is responsible for moving left horizontally.
                    y1_direction_change = 0
                # This Else If statement checks if the user has pressed down on the right arrow key.
                elif event.key == pygame.K_RIGHT:
                    # The snakes direction will now travel to the right horizontally, this is done by assigning the direction of the snake on the 'x'
                    # axis to travel to the 'snake_block', which is positive.
                    x1_direction_change = snake_block
                    # The vertical direction of the snake is left untouched as the right arrow key is responsible for the snake moving right.
                    y1_direction_change = 0
                # This Else If Statement checks if the user has pressed the up arrow key.
                elif event.key == pygame.K_UP:
                    # If the user has pressed the up arrow key, this will make the snake travel upwards on the game screen. It will move up by one block,
                    # which is why the '-snake_block' is used.
                    y1_direction_change = -snake_block
                    # The horizontal direction is left untouched.
                    x1_direction_change = 0
                # This Else If Statement checks if the user has pressed the down arrow key.
                elif event.key == pygame.K_DOWN:
                    # This will cause the snake to travel downwards along the game screen by one block, which is why the direction along the 'y' axis is now assigned
                    # to the 'snake_block' value.
                    y1_direction_change = snake_block
                    # The horizontal direction of the snake is left untouched.
                    x1_direction_change = 0

        # This if statement is responsible for checking if the snake has gone off of the game screen, which will result in the game ending.
        # The if statement checks if the 'x' postision and 'y' postision of the snake has exceeded the game displays width and height.
        if x1 >= game_display_width or x1 < 0 or y1 >= game_display_height + info_height or y1 < info_height:
            # If it has, the game is closed as the 'game_close' variable is now true.
            game_close = True
        # The 'x1' variable is updated to reflect the direction that the snake is travelling horizontally.
        x1 += x1_direction_change
        # The 'y1' variable is updated to reflect the direction that the snake is travelling vertically.
        y1 += y1_direction_change
        # The games display 'game_display' background is redrawn to reflect each 'frame' of the game.
        game_display.fill(blue_color)
        
        # This is where the food is drawn.
        pygame.draw.rect(game_display, red_color, [food_x, food_y, snake_block, snake_block])
        
        # This is where the super food is drawn.
        pygame.draw.circle(game_display, pink_color, (int(super_food_x + snake_block / 2), int(super_food_y + snake_block / 2)), snake_block // 2)

        # This is where the surface for the timer is drawn using 'blit'.
        game_display.blit(timer_surface, [280, 10])
        
        # This is where the surface for the high score is being drawn (blit).
        game_display.blit(high_score_surface, [140, 10])
        
        # The variable 'score_font' is responsible for storing the font that will be used for the score.
        score_font = pygame.font.SysFont(None, 25)
        # The variable 'score_text' is responsible for storing and rendering the font and text that will be displayed on the game screen to track the users score.
        score_text = score_font.render("Score: " + str(score), True, black_color)
        
        # The score's surface and rendered text is drawn on the game screen 'game_display' using the 'blit' method.
        game_display.blit(score_text, [5, 10])

        # This line of code will draw a line which seperates the game screen from the score menu.
        pygame.draw.line(game_display, black_color, (0, info_height), (game_display_width, info_height), 2)

        # The variable 'snake_Head' is currently an empty list responsible for storing the postision of the head of the snake.
        snake_Head = []
        
        # The current 'x' coordinate of the snakes head 'x1' is appended to the 'snake_Head' list.
        snake_Head.append(x1)

        # The current 'y' coordinate of the snakes head 'y1' is appended to the 'snake_Head' list.
        snake_Head.append(y1)

        # The 'snake_Head' list holding the current postision of the snake head is then appended to the 'snake_List' list.
        # This means that this list will now holds postisions of the snake in the form of '[x1, y1]', as each of the new snake
        # heads will result in a longer body of the snake.
        snake_List.append(snake_Head)
        # This if statement checks if the length 'len' of the snake list 'snake_List' is larger than the max length of the snake itself 'Length_of_snake'.
        if len(snake_List) > Length_of_snake:
            # If the length of the snake exceeds its max, the first (oldest/last) part of the snake is deleted.
            del snake_List[0]

        # This for loop iterates through each of the parts/segments of the snake, to see if the head of the snake has collided with its body.
        for x in snake_List[:-1]:
            # This if statement checks if the 'x' coordinate of the snakes body has made contact with its head.
            if x == snake_Head:
                # As a result this will close the current play of the game, which is why 'game_close' is re assigned to true.
                game_close = True

        # The 'the_snake_display' function is called, passing 'snake_block' and 'snake_List' as arguments.
        # This will render the snake onto the game display.
        the_snake_display(snake_block, snake_List)

        # The 'update' function from the 'pygame' framework is called on the 'pygame.display' to update the display window.
        pygame.display.update()

        # This if statement checks if the head of the snakes coordinates 'x1' and 'y1' has made contact with the food.
        if x1 == food_x and y1 == food_y:
            # If the snake has made contact with the food, the 'x' and 'y' coordinates of the food is redrawn at a random place on the game screen.
            food_x = round(random.randrange(0, game_display_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(info_height, game_display_height - snake_block) / 10.0) * 10.0
            # Since the snake has eaten a piece of food, this will cause the snake to grow by 2. The length of the snake is incremented by 2.
            Length_of_snake += 2
            # Since the user has eaten food, this will cause the score of the game to increment by 10.
            score = score + 10

        # The variable 'game_clock' which manages the timing of the game, is 'ticked' using the 'tick' method of the 'pygame' framework.
        # This controls the games frame rate, updatting the clock so the game executes at a number of frames per second where the number of 
        # frames is the value of 'snake_speed'.
        game_clock.tick(snake_speed)

        # This if statement checks if the head of the snakes coordinates 'x1' and 'y1' has made contact with the super food.
        if x1 == super_food_x and y1 == super_food_y:
            # If the snake has made contact with the super food, the 'x' and 'y' coordinates of the super food is redrawn at a random place on the game screen.
            super_food_x = round(random.randrange(0, game_display_width - snake_block) / 10.0) * 10.0
            super_food_y = round(random.randrange(info_height, game_display_height - snake_block) / 10.0) * 10.0
            # Eating the super food causes the snake to grow more than regular food, which is why the size/length of the snake is incremented by 5.
            Length_of_snake += 5
            # Eating the super food will also give the user a score boost of 50.
            score = score + 50
        
        # The variable 'game_clock' which manages the timing of the game, is 'ticked' using the 'tick' method of the 'pygame' framework.
        # This controls the games frame rate, updatting the clock so the game executes at a number of frames per second where the number of 
        # frames is the value of 'snake_speed'.
        game_clock.tick(snake_speed)

        # This while loop is responsible for displaying a game over screen to the user. This is indicated by the value of 'game_close' being true.
        while game_close == True:
            # The background of the game display 'game_display' is re-filled to the color blue 'blue_color'.
            game_display.fill(blue_color)
            # Each of the game over messages are rendered, each containing different text.
            game_over_message = font_type.render("Game Over!", True, black_color)
            game_over_message_two = font_type.render("Press 'Q' to quit!", True, black_color)
            game_over_message_three = font_type.render("Press 'R' to try again!", True, black_color)
            game_over_message_four = font_type.render("Press 'M' to return to menu!", True, black_color)
            # Each of the game over messages are drawn (blit) onto the game screen 'game_display'.
            game_display.blit(game_over_message, [50, 50])
            game_display.blit(game_over_message_two, [10, 70])
            game_display.blit(game_over_message_three, [10, 90])
            game_display.blit(game_over_message_four, [10, 110])

            # In order to see the messages and render the game over screen, the 'pygame' is updated.
            pygame.display.update()

            # This for loop controls the users next actions once the game over screen has been shown. The user can either retry, quit, or return to the main
            # menu to change the difficulty of the game. The loop iterates over each 'event' in the event queue.
            for event in pygame.event.get():
                # This if statement checks if the type of event was the user pressing a key.
                if event.type == pygame.KEYDOWN:
                    # This inner if statement checks if the user has pressed 'q', which means they want to quit the game alltogether.
                    if event.key == pygame.K_q:
                        # The 'game_over' variable is set to true as the game is over and the game will close.
                        game_over = True
                        # The 'game_close' variable is set to true as the game is closed.
                        game_close = False
                    # This if statement checks if the user has pressed the 'r' key, which means they want to retry and play again.
                    if event.key == pygame.K_r:
                        # Each of the game variables are reset to reflect the new game the user will be playing.
                        score = 0
                        start_time = time.time()
                        x1 = game_display_width / 2
                        y1 = game_display_height / 2
                        x1_direction_change = 0
                        y1_direction_change = 0
                        snake_List = []
                        Length_of_snake = 1
                        food_x = round(random.randrange(0, game_display_width - snake_block) / 10.0) * 10.0
                        food_y = round(random.randrange(0, game_display_height - snake_block) / 10.0) * 10.0
                        game_close = False
                    # This if statement cheks if the user has pressed the 'm' key, which means they want to return to the game menu.
                    if event.key == pygame.K_m:
                        # A call is made to the 'game_menu' function so the games menu is displayed.
                        game_menu()
                        # A call is made to the 'main_game_loop' function so after the game menu is displayed, the game will execute again.
                        main_game_loop()


    # This uninitializes each of the 'pygame' modules, and indictaes the game is ending.
    pygame.quit()
    # This exits python all together.
    quit()
# A call is made to the 'main_game_loop' function.
main_game_loop()
