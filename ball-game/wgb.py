from paddle import *
from ball import *
from collisionhandler import *
from wall import *
from highscore import *
from greenitem import *
from reditem import *
from itemcollisionhandler1 import *
from itemcollisionhandler2 import *

import inputbox
import random
import pygame
import time

def main():
    pygame.init()
    global jump_sound
    Jump_sound = pygame.mixer.Sound('Jump.wav')
    pygame.mixer.music.load('spelunk.mp3')
    pygame.mixer.music.play(-1)
    
    try:
        w = 640
        h = 480

        screen = pygame.display.set_mode((w, h))
        font = pygame.font.SysFont('Arial Black', 17)
        pygame.mouse.set_visible(False)
        clock = pygame.time.Clock()
        ch = CollisionHandler()
        itch1 = itemCollisionHandler1()
        itch2 = itemCollisionHandler2()

        TIMEEVENT = USEREVENT + 1
        pygame.time.set_timer(TIMEEVENT, 15)

        # Load our balls and add them to collision handler
        balls = Ball.createRandomBallsAsList(3, screen)
        for ball in balls:
            ch.addBall(ball)

        greenitems = Greenitem.createRandomItemsAsList1(1, screen)
        for greenitem in greenitems:
            itch1.addGreenitem(greenitem)

        reditems = Reditem.createRandomItemsAsList2(1, screen)
        for reditem in reditems:
            itch2.addReditem(reditem)
            

        # Insert walls and add them to collision handler
        walls = [
            Wall( screen, (0,30), (10, screen.get_height()) ), # Left wall
            Wall( screen, (screen.get_width()-10,30), (10, screen.get_height()) ), # Right wall
            Wall( screen, (0,30), (screen.get_width(), 10) ) # Top wall
        ]

        for wall in walls:
            ch.addObject(wall)
            itch1.addObject(wall)
            itch2.addObject(wall)
        
        # Create paddle and add it to collision handler
        paddle = Paddle(screen)
        ch.addObject(paddle)
        itch1.addObject(paddle)
        itch2.addObject(paddle)
        
        # Game variables
        run = True
        pause = False
        gameover = False
        viewHighScore = False;
        lifes = 3
        time = 0
        name = ""
        score = 0

        # Initialize highscore
        highscore = Highscore(screen)
		
        # Load scoreboard
        scoreBoard = font.render("Life: " + str(lifes) + " Score: ", True, (255, 0, 0))
        
        while not gameover:
        
            # Check for quits
            for event in pygame.event.get():
                
                # Quit-event
                if event.type == pygame.QUIT:
                    gameover = True
                    highscore.cur.close() # Close database connection
                    highscore.db.commit()
                    highscore.db.close()
                    
                if event.type == TIMEEVENT and not pause:
                    time += 1
                
                # Key presses
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        paddle.moveRight()
                            
                    elif event.key == K_LEFT:
                        paddle.moveLeft()

                    if event.key == K_i:
                       pause = not pause    
                        
                    if event.key == K_SPACE and not(run):
                        run = True
                        gameover = False
                        viewHighScore = False;
                        lifes = 3
                        time = 0
                        name = ""
                        score = 0
                        pygame.time.set_timer(TIMEEVENT, 15)

                        paddle.reset()
                        ch.reset()
                        itch1.reset()
                        itch2.reset()
                        
                        walls = walls[0:3]
                        for wall in walls:
                            ch.addObject(wall)
                            itch1.addObject(wall)
                            itch2.addObject(wall)

                        ch.addObject(paddle)
                        itch1.addObject(paddle)
                        itch2.addObject(paddle)
                        
                        
                        # Load our balls and add them to collision handler
                        balls = Ball.createRandomBallsAsList(3, screen)

                        greenitems = Greenitem.createRandomItemsAsList1(1, screen)

                        reditems = Reditem.createRandomItemsAsList2(1, screen)
                        
                        for ball in balls:
                            ch.addBall(ball)

                        for greenitem in greenitems:
                            itch1.addGreenitem(greenitem)

                        for reditem in reditems:
                            itch2.addReditem(reditem)
            
            if not pause:
                # Update positions for balls
                for ball in balls:
                    if ball.update(): # Returns true if ball goes below paddle-level
                        lifes -= 1

                for greenitem in greenitems:
                    if greenitem.update():
                        pass

                for reditem in reditems:
                    if reditem.update():
                        pass
            
            # Update collision handler
            if ch.update():
                score += 1
                pygame.mixer.Sound.play(Jump_sound)

            if itch1.update():
                score += 2
                paddle.bounceGreenItem()
                pygame.mixer.Sound.play(Jump_sound)

            if itch2.update():
                score -= 2
                if score < 0:
                    score = 0
                paddle.bounceRedItem()
                pygame.mixer.Sound.play(Jump_sound)
                
            # Draw background
            screen.fill((0, 0, 0))
            
            
            # Draw walls
            for wall in walls:
                wall.draw()
                
            # Draw paddle
            paddle.draw()    
            
            # Draw balls
            for ball in balls:
                ball.draw()

            # Draw items
            for greenitem in greenitems:
                greenitem.draw()

            for reditem in reditems:
                reditem.draw()

            #Draw scoreboard
            if run:
                scoreBoard = font.render("Life: " + str(lifes) + " Score: " + str(score), True, (255, 0, 0))

            pygame.draw.rect(screen, (30, 200, 10), (0, 0, time, 30))
            screen.blit(scoreBoard, (10, 5)) 

            # Level up!
            if time >= screen.get_width():
                time = 0
                action = random.randint(0, 1) # Randomize action
                paddle.levelup()
                
                if action == 0:
                    # Add new ball
                    balls.append(ch.addBall(Ball(screen, (random.randint(50, 550), random.randint(50, 200)), (randsign()*random.uniform(1.0,3.0),random.uniform(1.0,3.0)) )))
                    greenitems.append(itch1.addGreenitem(Greenitem(screen, (random.randint(50, 550), random.randint(50, 200)), (randsign()*random.uniform(1.0,3.0),random.uniform(1.0,3.0)) )))
                    reditems.append(itch2.addReditem(Reditem(screen, (random.randint(50, 550), random.randint(50, 200)), (randsign()*random.uniform(1.0,3.0),random.uniform(1.0,3.0)) )))
                elif action == 1:
                    # Add new wall, vertical or horizontal
                    if random.randint(0, 1):
                        walls.append(ch.addObject(Wall(screen, (random.randint(50, 550), random.randint(50, 200)), (200,10) )))
                        
                    else:
                        walls.append(ch.addObject(Wall(screen, (random.randint(50, 550), random.randint(50, 200)), (10,200) )))
                                     
                    # Add bonus item here
            # If lifes = 0    
            if lifes <= 0 and run:
                player = []
                pygame.time.set_timer(TIMEEVENT, 0)
                finalScore = score
                viewHighScore = True
                run = False
                name = inputbox.ask(screen, "Your name ")
                scoreBoard = font.render("Life: 0 Score: " + str(finalScore), True, (255, 0, 0))
                player = highscore.update(name, finalScore, font)
            
            # List highscore
            if viewHighScore:
                highscore.draw(player, font)
                
            # Print instructions
            if pause:
                font2 = pygame.font.SysFont('Arial Black', 40)
                trans = pygame.Surface((300, 350))
                trans.fill((0,0,0))
                pygame.Surface.convert_alpha(trans)
                trans.set_alpha(128)

                screen.blit(trans, (screen.get_width()/2-130,80))                                
                
                gameOverImg = font2.render("Instruction", True, (255, 0, 0))
                row1 = font.render("Game starts with 3 balls, Greenballs, Redballs", True, (255, 0, 0))
                row2 = font.render("Bounce theses balls as long as you can. ", True, (255,0,0) )
                row3 = font.render("If timebar is full,Then you either get a new ball or a new wall", True, (255,0,0) )
                row4 = font.render("Greenballs : score +2, paddle's width + 10", True, (255,0,0))
                row5 = font.render("Redballs : paddle's width - 20, score -2", True, (255,0,0))
                row6 = font.render("Press i to return to game.", True, (255,0,0) )
                
                screen.blit(gameOverImg, (screen.get_width()/2-150, 40))
                screen.blit(row1, (screen.get_width()/2-280, 140))
                screen.blit(row2, (screen.get_width()/2-280, 170))
                screen.blit(row3, (screen.get_width()/2-280, 200))
                screen.blit(row4, (screen.get_width()/2-280, 230))
                screen.blit(row5, (screen.get_width()/2-280, 260))
                screen.blit(row6, (screen.get_width()/2-280, 290))
                
            # Update screen
            pygame.display.flip()

            clock.tick(60)
            
    finally:
        pygame.quit()
        
        # Try close database connection
        try:
            highscore.db.close()
        except NameError:
            print("Ooops, no connection")

if __name__ == "__main__":
    main()
