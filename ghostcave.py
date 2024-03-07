#-----------------------------------------------------------------------------
# Program Name: GhostCave
# Purpose:     <A description of your program goes here.>
#
# Author:      SwayamShrimali
# Created:     23/11/2023
# Updated:     DD/MM/YYYY
#-----------------------------------------------------------------------------
#I think this project deserves a level 4+ because it has consistent coding comments, above and beyond code, a nice asthetic, music and is complete. The game itself is also polished.y
#
#
#List of level 3 expectations completed: All met
#Features Added Above Level 3 Expectations:
#   ... Multiple platforms
#   ... Multiple moving enemys
#   ... Advanced collition with multiple levels
#-----------------------------------------------------------------------------
# *********SETUP**********
import pygame # imports pygames library
pygame.init() #initilized pygame
pygame.display.set_caption("Ghost Cave")  # sets name for the window

# *********VARIABLES**********
# variables to set the size of the window
window_Width = 918  # sets width of screen
window_Height = 496  # sets height of screen
speed = 3  # sets speed for scrolling
jump_power = 16  # sets the power of the jump
gravity = 1  # sets the gravity effect
score = 0 #sets score for game


surface_Main = pygame.display.set_mode((window_Width, window_Height))  # create the window
clock = pygame.time.Clock()  # will allow us to set framerate

#***********Music*********

music = pygame.mixer.music.load("assets/Undertale.mp3") #loads music 
pygame.mixer.music.set_volume(0.5) #sets volume of music
pygame.mixer.music.play(loops=-1) #plays music in a loop

#********Text*********
# Set the font and color
font = pygame.font.Font('assets/Minecraft.ttf', 36) #import text for score
fontEnd = pygame.font.Font('assets/Minecraft.ttf', 60) #import text for ending screen
red = pygame.Color(255, 0, 0) #changes to Red color
green = pygame.Color(0, 255, 0) #changes to Green color

#********Starting Menu*******

menu_Not_Scaled = pygame.image.load("assets/MainMenu.001.png")  # loads the menu
menu = pygame.transform.scale2x(menu_Not_Scaled) #scales menu

#*******FLOOR*************
floor_Not_Scaled = pygame.image.load("assets/BackroundScrollV1.001.png")  # loads the bottom Floor
floor = pygame.transform.scale2x(floor_Not_Scaled) #dobles bottom floor size

floor_Not_Scaled_TOP = pygame.image.load("assets/BackroundScrollTOP.png")  # loads the top Floor
floor_TOP = pygame.transform.scale2x(floor_Not_Scaled_TOP) #dobles the top floor size

#*********Main Player*********

#Still
MainPlayerSmall = pygame.image.load("assets/Tiles/Tiles/Transparent/tile_0240.png")  # import our MC img Idel
MainPlayer = pygame.transform.scale2x(MainPlayerSmall) #dobles MC img idel

#MovingD
Player1Small = pygame.image.load("assets/Tiles/Tiles/Transparent/tile_0241.png")  # import our moving D MC
moving1 = pygame.transform.scale2x(Player1Small) #dobles MC moving img for D 

#MovingA
Player2Small = pygame.image.load("assets/Tiles/Tiles/Transparent/tile_0241.png")# import our MC img for moving D MC
Player2Flipped = pygame.transform.flip(Player2Small, True, False) #Flips it to become moving A MC
moving2 = pygame.transform.scale2x(Player2Flipped) #dobles MC moving img for A 

#Jumping 
PlayerJUMPSmall = pygame.image.load("assets/Tiles/Tiles/Transparent/tile_0244.png")  # import our MC img jumping
PlayerJUMPMoving = pygame.transform.scale2x(PlayerJUMPSmall)  #scales jumping img

MainPlayerX = 64 #Starting position for player X value
MainPlayerY = 190 #Starting position for player Y value
bg1 = 0 #Position of scrolling backround

moving = False #var for if moving
frame = 0 #frame number

player_animations = [MainPlayer, moving1, moving2, PlayerJUMPMoving] #all frames together grouped



#*******Belt*************

beltRaw = pygame.image.load("assets/Belt.png") #imports belt
belt = pygame.transform.scale2x(beltRaw) #scales belt

#******Decoration*********
grassRaw = pygame.image.load("assets/Grass.png") #import grass
grass = pygame.transform.scale2x(grassRaw) #scale grass

decorRaw = pygame.image.load("assets/Decor.png") #import decorations
decor = pygame.transform.scale2x(decorRaw) #scale decorations

fanRaw = pygame.image.load("assets/Fans.png") #import decorations
fan = pygame.transform.scale2x(fanRaw) #scale decorations



#*******Spike*************

spikeRaw = pygame.image.load("assets/Spike.png") #import spike
spike = pygame.transform.scale2x(spikeRaw) #scale spike

#*******Ending sign*************

endsighnRaw = pygame.image.load("assets/endingsighn.png") #import spike
endsighn = pygame.transform.scale2x(endsighnRaw) #scale spike

#*******Flying Enemy*********

flyingRawEn1 = pygame.image.load("assets/FlyingEn1.png") #import flying enemy
flyingEn1 = pygame.transform.scale2x(flyingRawEn1) #scale flying enemy
flyingEn2 = flyingRawEn1.copy() #duplicate enemy

flyingX = 1344 #position of first enemy
flyingY = 128 #position of both Y value for enemy
flying_direction = 1  # 1 for moving down, -1 for moving up




running = True #indicateds if running
scrolling_Right = False  # indicate whether scrolling is active
scrolling_Left = False  # indicate whether scrolling is active
is_jumping = False # indicates whether Jumping is active
on_ground = True  #indicates if on the ground
speed_boost = False #if touching conveyerbelt speed boost

game_over = False
won = False
start_game = False




# *********GAME LOOP**********
running = True
while running:
    # *********EVENTS**********
    if not game_over :
        score += 1
    
    for event in pygame.event.get():  # Check for Pygame events

        if event.type == pygame.QUIT:
                running = False  # Quit the game if the window is closed
        if event.type == pygame.KEYDOWN:     
            if event.key == pygame.K_y:
                start_game = True
            
            if event.key == pygame.K_m and won:
                    start_game = False
                    MainPlayerX = 64 #Starting position for player X value
                    MainPlayerY = 190 #Starting position for player Y value
                    bg1 = 0 #Position of scrolling backround
                    score = 0
                    won = False
                    game_over = False
                    running = True

        if start_game:

            if event.type == pygame.KEYDOWN and not won:
                if event.key == pygame.K_r:
                    game_over = False
                    MainPlayerX = 64 #Starting position for player X value
                    MainPlayerY = 190 #Starting position for player Y value
                    bg1 = 0 #Position of scrolling backround
                    score += 1000

                    
                if not game_over:
                    if event.key == pygame.K_d:
                        scrolling_Right = True  # Start scrolling right when 'D' key is pressed
                        moving = True
                        frame = 1  # Start with the first frame of the moving animation

                    if MainPlayerX >= 0:
                        if event.key == pygame.K_a:
                            scrolling_Left = True  # Start scrolling left when 'A' key is pressed
                            frame = 2


                    if event.key == pygame.K_w and not is_jumping:
                        is_jumping = True  # Trigger jump when 'W' key is pressed

                    if event.key == pygame.K_w and event.key == pygame.K_d:
                        frame = 4  # Adjust frame for diagonal movement
                    elif event.key == pygame.K_w and event.key == pygame.K_a:
                        frame = 5  # Adjust frame for diagonal movement

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    scrolling_Right = False  # Stop scrolling right when 'D' key is released
                    moving = False
                    frame = 0  # Set frame to idle
                if event.key == pygame.K_a:
                    scrolling_Left = False  # Stop scrolling left when 'A' key is released
                    moving = False
                    frame = 0  # Set frame to idle

    try:
        # Collision Mech
        if surface_Main.get_at((MainPlayerX, MainPlayerY + MainPlayer.get_height())) == (255, 255, 255, 255):
            MainPlayerY -= 2  # Adjust position to avoid collision
            on_ground = True
        if surface_Main.get_at((MainPlayerX + MainPlayer.get_width(), MainPlayerY + MainPlayer.get_height())) == (255, 255, 255, 255):
            MainPlayerY -= 2  # Adjust position to avoid collision
            on_ground = True

        # BeltCollition
        player_rect = MainPlayer.get_rect(topleft=(MainPlayerX, MainPlayerY))
        belt_rect = belt.get_rect(topleft=(bg1 + 475, 370))
        if player_rect.colliderect(belt_rect):
            MainPlayerY -= 2  # Adjust position to avoid collision with the belt
            on_ground = True
            speed_boost = True  # Player is touching the belt
        else:
            speed_boost = False  # Player is not touching the belt

        # SpikeCollition: if touch player trigger game_over
        spike_rect = spike.get_rect(topleft=(bg1 + 590, 464))
        if player_rect.colliderect(spike_rect):
            # RESPAWN
            if not game_over :
                score += 100
            game_over = True

        # SpikeContinued: if player below 448: trigger game_over
        if MainPlayerY >= 448:
            if not game_over :
                score += 100
            game_over = True
        
        # endSighnCollition: if touch player trigger game_over
        sighn_rect = endsighn.get_rect(topleft=(bg1+ 2336, 96))
        if player_rect.colliderect(sighn_rect):
            # add score + respawn
            won = True
            if not game_over :
                score -= 500
            game_over = True

    except: #failsafe for any buggs or errors
        game_over = True

    # Jumping Mech
    if is_jumping and on_ground:
        MainPlayerY -= jump_power
        jump_power -= gravity
    if jump_power <= 0:
        is_jumping = False
        jump_power = 15
        on_ground = False  # Update on_ground when the jump is completed

    # Scrolling Mechanic
    if scrolling_Right:
        if speed_boost:
            bg1 -= (speed + 12)
        elif not speed_boost and bg1 < -1400 and bg1 > -1800:
            bg1 -= (speed - 1.8)
        elif not speed_boost and bg1 < -1800:
            bg1 -= 3
        else:
            bg1 -= 3

    if scrolling_Left:
        bg1 += speed + (12 if speed_boost else 0)
        

    # Falling Mech
    MainPlayerY = MainPlayerY + 2

    # Enemy Flying Mech
    flyingY += 1 * flying_direction

    # FlyingEnemyCollition
    flyingen_rect = flyingEn1.get_rect(topleft=(flyingX + bg1, flyingY))
    if player_rect.colliderect(flyingen_rect):
        # RESPAWN
        game_over = True

    flyingen_rect = flyingEn1.get_rect(topleft=(1098 + bg1, flyingY))
    if player_rect.colliderect(flyingen_rect):
        # RESPAWN
        game_over = True

    if flyingY > 320:
        flying_direction = -1
    elif flyingY < 160:
        flying_direction = 1

    # *********BLOCK WALKING OFF************
    if bg1 >= 1:
        bg1 -= bg1  # Reset background position
    #*********Score**************
    text = font.render(f"Time: {score}!", True, red)

    # *********DRAW THE FRAME********** 
    surface_Main.fill((0, 0, 0))  # Set background color

    surface_Main.blit(floor, (bg1, 5))  # Draw floor
    surface_Main.blit(floor_TOP, (bg1, 5))  # Draw top part of the floor

    surface_Main.blit(belt, (bg1 + 475, 370))  # Draw belt
    surface_Main.blit(grass, (bg1 + 352, 291))  # Draw grass
    surface_Main.blit(grass, (bg1 + 320, 196))  # Draw grass
    surface_Main.blit(decor, (bg1, 0))  # Draw decor
    surface_Main.blit(fan, (bg1+1920, 224))  # Draw fans

    surface_Main.blit(endsighn, (bg1+ 2336, 96))  # Draw ending sighn

    spike_positions = [590, 960, 1056, 1152, 1248, 1344, 1440, 1536, 1632, 1728, 1824, 1920, 2016, 2112, 2208]

    for spike_pos in spike_positions:
        surface_Main.blit(spike, (bg1 + spike_pos, 464))  # Draw spikes

    surface_Main.blit(player_animations[frame], (MainPlayerX, MainPlayerY))  # Draw player animation

    surface_Main.blit(flyingEn1, (flyingX + bg1, flyingY))  # Draw flying enemy
    surface_Main.blit(flyingEn1, (1098 + bg1, flyingY))  # Draw flying enemy

    surface_Main.blit(text, (0, 0)) #print score
 
    if game_over and not won: #if died without winning MSG
        textEnd = fontEnd.render(f"Game over!", True, red)
        textEnd2 = fontEnd.render(f"You took: {score} seconds", True, red)
        textEnd3 = fontEnd.render(f"Press R to restart", True, red)
        surface_Main.blit(textEnd, (128,200)) #print Game over
        surface_Main.blit(textEnd2, (128, 248)) #print You took: {score} seconds
        surface_Main.blit(textEnd3, (128, 296)) #print Press R to restart
    elif game_over and won: #if died with winning MSG
        textEnd = fontEnd.render(f"Good Job!", True, green)
        textEnd2 = fontEnd.render(f"Your score is: {score}", True, green)
        textEnd3 = fontEnd.render(f"Press M for main menu", True, green)
        surface_Main.blit(textEnd, (96,200)) #print Good Job
        surface_Main.blit(textEnd2, (96, 248)) #print You took: {score} seconds only
        surface_Main.blit(textEnd3, (96, 296)) #print Press M for main menu

    if not start_game:
        surface_Main.blit(menu, (0,0)) #draw menu
        score = 0
    # *********End Settings**********
    pygame.display.flip()  # Update the display
    clock.tick(60)  # Force frame rate to 60fps or lower

pygame.quit()  # Quit Pygame