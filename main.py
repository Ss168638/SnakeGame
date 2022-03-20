import pygame
import random
from pygame.locals import *


#init pygame
pygame.init()

WIDTH , HEIGHT = 400, 400
width, height = 20, 20

FRAME_RATE = 30

BG_COLOR = (0, 0, 0)
RECT_COLOR = (0, 255, 0)




WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# RECT_BOX = pygame.Rect(left, top, width, height)

class FOOD:
    def __init__(self, eaten):
        self.eaten = eaten
        self.food_x = random.randint(0, WIDTH)
        self.food_y = random.randint(0, HEIGHT)
        self.food = (self.food_x, self.food_y)
        self.FOOD_SIZE = 10
        self.FOOD_COLOR = (255, 0, 0)

    def generate_food(self, win):
        if self.eaten == 1:
            self.food_x = random.randint(0, WIDTH)
            self.food_y = random.randint(0, HEIGHT)
            self.food = (self.food_x, self.food_y)
        pygame.draw.circle(win, self.FOOD_COLOR, self.food, self.FOOD_SIZE)



class SNAKE:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def draw_rect(self, win):
        self.rect = pygame.Rect(self.x, self.y, width, height)
        pygame.draw.rect(win, RECT_COLOR, self.rect)
    
    def move_down(self, win, speed):
        if self.y == WIDTH:
            self.y = 0
        else:
            self.y += speed

    def move_up(self, win, speed):
        if self.y == 0:
            self.y = HEIGHT
        else:
            self.y -= speed

    def move_left(self, win, speed):
        if self.x == 0:
            self.x = WIDTH
        else:
            self.x -= speed

    def move_right(self, win, speed):
        if self.x == WIDTH:
            self.x = 0
        else:
            self.x += speed



def eventLoop():

    run = True
    count = 1
    clock = pygame.time.Clock()
    snake = SNAKE(10, 10)
    food = FOOD(False)
    SPEED = 2
    up, down, left, right = 0, 0, 0, 0

    while run:
        clock.tick(FRAME_RATE)
        WIN.fill(BG_COLOR)
        snake.draw_rect(WIN)
        food.generate_food(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    up, down, left, right = 0, 1, 0, 0
                    # snake.move_down(WIN, SPEED)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    up, down, left, right = 1, 0, 0, 0
                    # snake.move_up(WIN, SPEED)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    up, down, left, right = 0, 0, 1, 0
                    # snake.move_left(WIN, SPEED)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    up, down, left, right = 0, 0, 0, 1
                    # snake.move_right(WIN, SPEED)
        if down == 1:
            snake.move_down(WIN, SPEED)
            # SPEED += 1
        elif up == 1:
            snake.move_up(WIN, SPEED)
            # SPEED += 1
        elif left == 1:
            snake.move_left(WIN, SPEED)
            # SPEED += 1
        elif right == 1:
            snake.move_right(WIN, SPEED)
            # SPEED += 1
        else:
            pass

        if food.eaten == True:
            food.generate_food(WIN)
            food.eaten = False
        snake.draw_rect(WIN)
        pygame.display.update()


    pygame.quit()


if __name__ == "__main__":
    jls_extract_var = eventLoop
    jls_extract_var()