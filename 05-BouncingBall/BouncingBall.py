import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move
class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.radius = random.randint(10, 30)
        self.x = random.randint(self.radius, self.screen.get_width()-self.radius)
        self.y = random.randint(self.radius, self.screen.get_height()-self.radius)
        self.x_speed = random.randint(-4, 5)
        self.y_speed = random.randint(-4, 5)
        while self.x_speed == 0 and self.y_speed == 0:
            self.x_speed = random.randint(-5, 5)
            self.y_speed = random.randint(-5, 5)

        self.color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))


    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius, 0)

    def move(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed
        if self.x - self.radius < 0 or self.x + self.radius > self.screen.get_width():
            self.x_speed = -self.x_speed
        if self.y - self.radius < 0 or self.y + self.radius > self.screen.get_height():
            self.y_speed = -self.y_speed

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    balls = []

    for k in range(100):
        ball = Ball(screen)
        balls.append(ball)
        print(k)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))
        for ball in balls:
            ball.move()
            ball.draw()

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
