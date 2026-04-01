import pygame
import random

# Initialize pygame
pygame.init()

# Screen size
width = 600
height = 400
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Car Racing Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
blue = (50, 153, 213)

# Clock
clock = pygame.time.Clock()

# Car settings
car_width = 50
car_height = 80

def car(x, y):
    pygame.draw.rect(game_window, blue, [x, y, car_width, car_height])

def obstacle(obs_x, obs_y, obs_w, obs_h):
    pygame.draw.rect(game_window, red, [obs_x, obs_y, obs_w, obs_h])

def gameLoop():
    x = width // 2
    y = height - car_height - 10
    x_change = 0

    obs_x = random.randint(0, width - 50)
    obs_y = -100
    obs_w = 50
    obs_h = 80
    obs_speed = 7

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        game_window.fill(white)

        car(x, y)
        obstacle(obs_x, obs_y, obs_w, obs_h)
        obs_y += obs_speed

        # Collision check
        if y < obs_y + obs_h and y + car_height > obs_y:
            if x < obs_x + obs_w and x + car_width > obs_x:
                print("💥 Crash! Game Over")
                game_exit = True

        # Reset obstacle
        if obs_y > height:
            obs_y = -100
            obs_x = random.randint(0, width - obs_w)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

gameLoop()
