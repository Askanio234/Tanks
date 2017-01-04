# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 20:34:28 2016

@author: Askanio
"""

import pygame
import random

pygame.init()
#Defining colors
white = (255,255,255)
black = (0,0,0)
red = (200,0,0)
light_red = (255,0,0)
green = (0,155,0)
light_green = (0,255,0)
yellow = (200,200,0)
light_yellow = (255,255,0)
#Defining resolution
display_width = 800
display_height = 600

#Game display size
gameDisplay = pygame.display.set_mode((display_width,display_height))
#Game name & game icon (will be displayed on game window)
pygame.display.set_caption('Tanks!')
#icon = pygame.image.load('apple.png')
#pygame.display.set_icon(icon)
#loading snakeheadsprite

#defining clock as pygame in-built function
clock = pygame.time.Clock()
FPS = 15


#Tank size
tank_width = 40
tank_height = 20
turret_width = 5
wheel_width = 5

#Rounding function to the next 10s so stuff will be perfectly alligned
def roundToNextTen(n):
    """This function will round int to nearest 10 usefull when"""
    return round(n/10.0)*10.0

#Defining a functions to print message to the sreen
def text_objects(text, color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonX, buttonY, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonX+(buttonwidth/2)),buttonY+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()
            if action == "controls":
                game_controls()
            if action == "play":
                gameLoop()
            if action == "main":
                game_intro()
            
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))
    text_to_button(text,black,x,y,width,height)
    
smallfont = pygame.font.SysFont("comicsansms",25)
medfont = pygame.font.SysFont("comicsansms",50)
largefont = pygame.font.SysFont("comicsansms",80)

def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Paused",
                          black,
                          -100,
                          size = "large")
        message_to_screen("Press C to continie or Q to quit.",
                          black,
                          25)
        pygame.display.update()
        clock.tick(5)
        
def score(score):
    text = smallfont.render("Score: " + str(score), True, black)
    gameDisplay.blit(text, [0,0])

def barrier(x_location, random_height):
   
    
    pygame.draw.rect(gameDisplay, green, 
                     [
                     x_location,display_height-random_height, 50, 
                     random_height
                        ])

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
                    
        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks!",
                          green,
                          -100,
                          "large")
        message_to_screen("The objective is to shot and destroy",
                          black,
                          -30)
        message_to_screen("the enemy tank before they destroy you",
                          black,
                          10)
        message_to_screen("The more enemies you destroy, the harder they get!",
                          black,
                          50)
#        message_to_screen("Press C to play, P to pause or Q to quit",
#                          black,
#                          180)
        
        
        button("Play", 150, 500, 100, 50,green,light_green, action = "play")
        button("Controls", 350,500,100,50,yellow,light_yellow, action = "controls")
        button("Quit", 550,500,100,50,red,light_red, action = "quit")
        
        pygame.display.update()
        clock.tick(30)

def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg ,color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def tank(x,y, turret_position):
    x = int(x)
    y = int(y)
        
    possible_turrets = [
                        (x-27, y-2),
                        (x-26, y-5),
                        (x-25, y-8),
                        (x-23, y-12),
                        (x-20, y-14),
                        (x-18, y-15),
                        (x-15, y-17),
                        (x-13, y-19),
                        (x-11, y-21)
                        ]
    
    pygame.draw.circle(gameDisplay, black, (x,y), int(tank_height/2))
    pygame.draw.rect(gameDisplay, black, (x-tank_height, y, tank_width, tank_height))
    pygame.draw.line(gameDisplay, black, (x,y), possible_turrets[turret_position], turret_width)
    pygame.draw.circle(gameDisplay, black, (x-15, y+20), wheel_width)
    pygame.draw.circle(gameDisplay, black, (x-10, y+20), wheel_width)
    pygame.draw.circle(gameDisplay, black, (x-5, y+20), wheel_width)
    pygame.draw.circle(gameDisplay, black, (x, y+20), wheel_width)
    pygame.draw.circle(gameDisplay, black, (x+5, y+20), wheel_width)
    pygame.draw.circle(gameDisplay, black, (x+10, y+20), wheel_width)
    pygame.draw.circle(gameDisplay, black, (x+15, y+20), wheel_width)
    
    
def game_controls():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
           
                    
        gameDisplay.fill(white)
        message_to_screen("Controls",
                          green,
                          -100,
                          "large")
        message_to_screen("Fire: Spacenar",
                          black,
                          -30)
        message_to_screen("Move Turret: UP and Down arrows",
                          black,
                          10)
        message_to_screen("Move Tank: Left and Right arrows",
                          black,
                          50)
        message_to_screen("Pause: P",
                          black,
                          90)
        
        
        button("Play", 150, 500, 100, 50,green,light_green, action = "play")
        button("Main", 350,500,100,50,yellow,light_yellow, action = "main")
        button("Quit", 550,500,100,50,red,light_red, action = "quit")
        
        pygame.display.update()
        clock.tick(30)

#Main Loop
def gameLoop():
    running = True
    gameOver = False
    FPS = 15
    
    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tank_move = 0

    current_turret_position = 0
    change_turret = 0
     
    x_location = (display_width/2) 
    + random.randint(-0.2*display_width, 0.2*display_width)
    random_height = random.randrange(display_height*0.1,display_height*0.6)
    
    while running:
        while gameOver:
            gameDisplay.fill(white)
            message_to_screen("Game over", 
                              red, 
                              -50, 
                              size = "large")
            message_to_screen("Press C to play again or Q to quit", 
                              black, 
                              50, 
                              size = "medium")
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
             
        #Checking for events
        for event in pygame.event.get():
            #Moving the Tank
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tank_move = -5
                elif event.key == pygame.K_RIGHT:
                    tank_move = 5
                elif event.key == pygame.K_UP:
                    change_turret = 1
                elif event.key == pygame.K_DOWN:
                    change_turret = -1
                elif event.key == pygame.K_p:
                    pause()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tank_move = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    change_turret = 0
            #Quiting the game
            if event.type == pygame.QUIT:
                running = False
                
        
        #Changing color of display
        gameDisplay.fill(white)
        
        #Rendering graphics
        mainTankX += tank_move
        current_turret_position += change_turret
        if current_turret_position > 8:
            current_turret_position = 8
        elif current_turret_position < 0:
            current_turret_position = 0
        tank(mainTankX,mainTankY, current_turret_position)
        barrier(x_location, random_height)
        
        
                
        
    
       
        pygame.display.update()
        #Updating clock No. of ticks = FPS
        clock.tick(FPS)
    pygame.quit()
    quit()
    
game_intro()         
gameLoop()            
          

