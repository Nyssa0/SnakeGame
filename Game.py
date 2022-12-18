# importing libraries
import pygame
import numpy

from ColorClass import Color
from FruitClass import Fruit
from PlayerClass import Player
from RulesClass import Rules
from ScoreClass import Score
from ScreenClass import Screen
from SnakeClass import Snake

snake = Snake()
screen = Screen()
color = Color()
player = Player()

# Initialising pygame
pygame.init()

# Initialise game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((screen.x, screen.y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

bonus = Fruit(screen.x, screen.y, pygame.image.load('images/bonus.png'))
bonus.new_position(screen.x, screen.y)
malus = Fruit(screen.x, screen.y, pygame.image.load('images/malus.png'))
malus.new_position(screen.x, screen.y)
if player.difficulty != 3:
    health = Fruit(screen.x, screen.y, pygame.image.load('images/hp.webp'))
    health.new_position(screen.x, screen.y)

change_to = snake.direction
score = Score()
rules = Rules()

while True:

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two directions
    # simultaneously
    if change_to == 'UP' and snake.direction != 'DOWN':
        snake.direction = 'UP'
    if change_to == 'DOWN' and snake.direction != 'UP':
        snake.direction = 'DOWN'
    if change_to == 'LEFT' and snake.direction != 'RIGHT':
        snake.direction = 'LEFT'
    if change_to == 'RIGHT' and snake.direction != 'LEFT':
        snake.direction = 'RIGHT'

    # Moving the snake
    if snake.direction == 'UP':
        snake.position[1] -= 10
    if snake.direction == 'DOWN':
        snake.position[1] += 10
    if snake.direction == 'LEFT':
        snake.position[0] -= 10
    if snake.direction == 'RIGHT':
        snake.position[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores will be
    # incremented by 10
    snake.body.insert(0, list(snake.position))
    if snake.position[0] == bonus.position[0] and snake.position[1] == bonus.position[1]:
        score.point, snake.speed = bonus.get_bonus(score.point, player.difficulty, snake.speed)
    elif snake.position[0] == malus.position[0] and snake.position[1] == malus.position[1]:
        score.point, snake.speed = malus.get_malus(score.point, player.difficulty, snake.speed)
    elif player.difficulty != 3 and snake.position[0] == health.position[0] and snake.position[1] == health.position[1]:
        player.hp = health.get_health(player.hp)
    else:
        snake.body.pop()

    bonus.fruit_spawn(screen.x, screen.y)
    malus.fruit_spawn(screen.x, screen.y)

    if player.difficulty != 3:
        health.fruit_spawn(screen.x, screen.y)

    game_window.fill(color.background)

    for pos in snake.body:
        pygame.draw.rect(game_window, color.snake, pygame.Rect(
            pos[0], pos[1], 10, 10))

    pygame.draw.rect(game_window, color.background, pygame.Rect(
        bonus.position[0], bonus.position[1], 10, 10))

    pygame.draw.rect(game_window, color.background, pygame.Rect(
        malus.position[0], malus.position[1], 10, 10))

    if player.difficulty != 3:
        pygame.draw.rect(game_window, color.background, pygame.Rect(
            health.position[0], health.position[1], 10, 10))

    # Game Over conditions
    if snake.position[0] < 0 or snake.position[0] > screen.x - 10:
        rules.game_over(score.point, color.red, screen.x, screen.y, game_window)
    if snake.position[1] < 0 or snake.position[1] > screen.y - 10:
        rules.game_over(score.point, color.red, screen.x, screen.y, game_window)
    if player.hp == 0:
        rules.game_over(score.point, color.red, screen.x, screen.y, game_window)
    if score.point < 0:
        score.point = 0
        rules.game_over(score.point, color.red, screen.x, screen.y, game_window)

    # Touching the snake body
    for block in snake.body[1:]:
        if snake.position[0] == block[0] and snake.position[1] == block[1]:
            rules.game_over(score.point, color.red, screen.x, screen.y, game_window)

    # displaying score continuously
    score.show_score(1, color.white, 'times new roman', 20, score.point, game_window)
    player.show_hp(1, color.white, 'times new roman', 20, player.hp, game_window, screen.x, 0)

    bonus.show_fruit(game_window, color.background)
    malus.show_fruit(game_window, color.background)
    if player.difficulty != 3:
        health.show_fruit(game_window, color.background)

    pygame.display.update()

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    fps.tick(snake.speed)
