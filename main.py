import pygame
import random

#initializing pygame
pygame.init()

width , height = 400, 400
SCALE = 20
iterator = []   #iterator for Grid Points
#storing random values to generate snake food
for value in range(0, (width//SCALE)*(height//SCALE)):
    iterator.append(random.randint(1, (width//SCALE)*(height//SCALE)-SCALE))

#setting the window size
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

welcome_surf = pygame.Surface((width, height))
welcome_rect = welcome_surf.get_rect()

grid_surf = pygame.Surface((width,height))

#text font
text_font = pygame.font.Font(None, 30)

#Snake Class
class SNAKE:
    def __init__(self, x, y, xwidth, yheight):
        self.x = x
        self.y = y
        self.xwidth = xwidth
        self.yheight = yheight
        self.total = 0
        self.color = (255,255,51)
        self.foodcolor = (220,20,60)
        self.tail = []
        self.foodx = 0
        self.foody = 0
        self.foodwidth = 0
        self.foodheight = 0
        self.eaten = False
        self.grid = []
        self.SCORE = 0
        self.FRAME_RATE = 5
    #to draw snake head
    def drawRect(self, win):
        rect = pygame.Rect(self.x, self.y, self.xwidth, self.yheight)
        pygame.draw.rect(win, self.color, rect)
        win.blit(win, (0, 0))
        pygame.display.flip()
        if self.total > 0:
            self.tail.append(rect)

    def moveUP(self):
        if self.y == 0:
            self.y = height
        else:
            self.y -= SCALE

    def moveLEFT(self):
        if self.x == 0:
            self.x = width
        else:
            self.x -= SCALE

    def moveDown(self):
        if self.y == height:
            self.y = 0
        else:
            self.y += SCALE
            
    def moveRIGHT(self):
        if self.x == width:
            self.x = 0
        else:
            self.x += SCALE
    #to draw snake food
    def drawfood(self, win, value):
        index = iterator[value]
        self.foodx, self.foody, self.foodwidth, self.foodheight = self.grid[index]
        rect = pygame.Rect(self.foodx, self.foody, self.foodwidth, self.foodheight)
        self.foodcolor = (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))
        pygame.draw.rect(win, self.foodcolor, rect)
        win.blit(win, (0, 0))
        pygame.display.flip()

    #check for food eaten
    def foodeaten(self):
        snakerect = pygame.Rect(self.x, self.y, self.xwidth, self.yheight)
        foodrect = pygame.Rect(self.foodx, self.foody, self.foodwidth, self.foodheight)
        if snakerect.colliderect(foodrect) == True:
            self.total += 1
            self.color = self.foodcolor
            return True
        return False
    #check snake head collision with body
    def bodycollisioncheck(self):
        if len(self.tail) > 4:
            snakerect = pygame.Rect(self.x, self.y, self.xwidth, self.yheight)
            for tail in self.tail[:-1]:
                tailrect = pygame.Rect(tail[0], tail[1], tail[2], tail[3])
                if snakerect.colliderect(tailrect) == True:
                    print("Game Over")
                    self.total = 0
                    return True
        return False

    #drawing the Grid Layout
    def drawgrid(self, surface):
        size = 20
        for rows in range(0, width//SCALE, 1):
            for cols in range(0, height//SCALE, 1):
                rect = pygame.Rect(rows*size, cols*size, size, size)
                pygame.draw.rect(surface, (0, 100, 0), rect, 1)
                self.grid.append(rect)

    #drawing body of snake
    def drawTail(self, win):
        for i in range(len(self.tail)-1):
            self.tail[i] = self.tail[i+1]
        self.tail = self.tail[:self.total]
        for tail in self.tail:
            pygame.draw.rect(win, self.color, tail)
            win.blit(win, (0, 0))
            pygame.display.flip()

    def get_score(self, score):
        #score surface
        score_surf = text_font.render(f"Score : {score}", False, "Green")
        score_rect = score_surf.get_rect(center = (width/2, SCALE))
        return score_surf, score_rect
    def declare_winner(self):
        winner_surf = text_font.render("Hurray!!!, You Won.", False, "Green")
        winner_rect = winner_surf.get_rect(center = (width/2 + SCALE, height/6))
        return winner_surf, winner_rect

    def declare_loser(self):
        loser_surf = text_font.render("Awwhh!!!, You Lose.", False, "Green")
        loser_rect = loser_surf.get_rect(center = (width/2 + SCALE, height/6))
        return loser_surf, loser_rect

    def start_game_text(self):
        if (self.SCORE > 0 and self.SCORE < 45) or self.SCORE == 45:
            start_surf = text_font.render("Press SPACE to Start the Game Again.", False, "Green")
            start_rect = start_surf.get_rect(center = (width/2, height/2 + SCALE * 5))
            return start_surf, start_rect
        else:
            start_surf = text_font.render("Press SPACE to Start the Game.", False, "Green")
            start_rect = start_surf.get_rect(center = (width/2, height/2 + SCALE * 5))
            return start_surf, start_rect
    
    #snake image
    def draw_snake_img(self):
        snake_surf = pygame.image.load("SnakeGame\snake.png").convert_alpha()
        snake_surf = pygame.transform.scale(snake_surf, (width/2, height/2 - SCALE))
        snake_rect = snake_surf.get_rect(center = (width/2 + SCALE, height/2 - SCALE))
        return snake_surf, snake_rect

#Main event Loop for Game
def eventloop():
    seed = 4
    run = True
    game_active = False
    clock = pygame.time.Clock()
    up, left, down, right = 0, 0, 0, 0
    snake = SNAKE(0+SCALE, 0+SCALE, SCALE, SCALE)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and game_active == True:
                if event.key == pygame.K_UP and down == False:
                    up, left, down, right = 1, 0, 0, 0
                    print("Snake moved up!")
                elif event.key == pygame.K_LEFT and right == False:
                    up, left, down, right = 0, 1, 0, 0
                    print("Snake moved left!")
                elif event.key == pygame.K_DOWN and up == False:
                    up, left, down, right = 0, 0, 1, 0
                    print("Snake moved down!")
                elif event.key == pygame.K_RIGHT and left == False:
                    up, left, down, right = 0, 0, 0, 1
                    print("Snake moved right!")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and game_active == False:
                if snake.SCORE > 0: snake.SCORE = 0
                game_active = True
        if game_active:
            snake.drawgrid(grid_surf)
            WIN.blit(grid_surf, (0, 0))
            score_surf, score_rect = snake.get_score(snake.SCORE)
            WIN.blit(score_surf, score_rect)
            
            snake.eaten = snake.foodeaten()
            if (snake.eaten == True):
                snake.SCORE += 1
                snake.eaten == False
                seed += 3

            if snake.bodycollisioncheck() == True:
                game_active = False

            if up == True:
                snake.moveUP()
            elif left == True:
                snake.moveLEFT()
            elif down == True:
                snake.moveDown()
            elif right == True:
                snake.moveRIGHT()

            if snake.SCORE == 5:
                snake.FRAME_RATE = 6
            elif snake.SCORE == 10:
                snake.FRAME_RATE = 7
            elif snake.SCORE == 15:
                snake.FRAME_RATE = 8
            elif snake.SCORE == 20:
                snake.FRAME_RATE = 9
            elif snake.SCORE == 25:
                snake.FRAME_RATE = 10
            elif snake.SCORE == 30:
                snake.FRAME_RATE = 11
            elif snake.SCORE == 35:
                snake.FRAME_RATE = 12
            elif snake.SCORE == 40:
                snake.FRAME_RATE = 13
            elif snake.SCORE == 45:
                snake.FRAME_RATE = 5
                game_active = False

            snake.drawfood(WIN, seed)
            snake.drawTail(WIN)
            snake.drawRect(WIN)
            pygame.display.flip()
        else:
            WIN.fill('Yellow')
            snake_surf, snake_rect = snake.draw_snake_img()
            WIN.blit(snake_surf, snake_rect)
            if snake.SCORE == 45:
                score_surf, score_rect = snake.get_score(snake.SCORE)
                WIN.blit(score_surf, score_rect)
                winner_surf, winner_rect = snake.declare_winner()
                WIN.blit(winner_surf, winner_rect)
                start_surf, start_rect = snake.start_game_text()
                WIN.blit(start_surf, start_rect)
            elif snake.SCORE > 0 and snake.SCORE < 45:
                score_surf, score_rect = snake.get_score(snake.SCORE)
                WIN.blit(score_surf, score_rect)
                loser_surf, loser_rect = snake.declare_loser()
                WIN.blit(loser_surf, loser_rect)
                start_surf, start_rect = snake.start_game_text()
                WIN.blit(start_surf, start_rect)
            else:
                start_surf, start_rect = snake.start_game_text()
                WIN.blit(start_surf, start_rect)

        clock.tick(snake.FRAME_RATE)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    eventloop()