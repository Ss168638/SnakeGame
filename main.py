import pygame
import random
#initializing pygame
pygame.init()

width , height = 400, 400
FRAME_RATE = 4
SCALE = 20
iterator = []   #iterator for Grid Points
#storing random values to generate snake food
for value in range(0, (width//SCALE)*(height//SCALE)):
    iterator.append(random.randint(1, (width//SCALE)*(height//SCALE)-SCALE))

#setting the window size
WIN = pygame.display.set_mode((width, height))

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

#Main event Loop for Game
def eventloop():
    seed = 4
    run = True
    clock = pygame.time.Clock()
    up, left, down, right = 0, 0, 0, 0
    snake = SNAKE(0+SCALE, 0+SCALE, SCALE, SCALE)
    grid_surf = pygame.Surface((width,height))
    snake.drawgrid(grid_surf)
    WIN.blit(grid_surf, (0, 0))
    pygame.display.flip()

    while run:
        clock.tick(FRAME_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
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

        snake.eaten = snake.foodeaten()
        if (snake.eaten == True):
            snake.eaten == False
            seed += 3

        if snake.bodycollisioncheck() == True:
            run = False

        if up == True:
            snake.moveUP()
        elif left == True:
            snake.moveLEFT()
        elif down == True:
            snake.moveDown()
        elif right == True:
            snake.moveRIGHT()
            
        WIN.blit(grid_surf, (0, 0))
        pygame.display.flip()
        snake.drawfood(WIN, seed)
        snake.drawTail(WIN)
        snake.drawRect(WIN)
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    eventloop()