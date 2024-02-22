import pygame
import random
from sprite import Sprite
import input
import ball
import ai

# Initialize Pygame
pygame.init()

# Set up the window
window_width = 800
window_height = 600
key_state = {}
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong")
gBall = Sprite("ball", 40, 40, window_width/2, window_height/2)
paddle = Sprite("rect", 15, 160, 80, window_height/2 - 80)
paddle2 = Sprite("rect", 15, 160, window_width - 80, window_height/2 - 80)
paddle.SetControllable()
ballSpeed = random.uniform(1.75, 2.25)
vballSpeed = random.uniform(0.3, 1)
# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            key_state[event.key] = True
            print("Key pressed.")
        elif event.type == pygame.KEYUP:
            key_state[event.key] = False
    input.UpdateInput(key_state)
    ai.UpdateAIMovement(paddle2, gBall, 2)
    ballSpeed, vballSpeed, over = ball.UpdatePhysics(gBall, window_width, window_height, ballSpeed, vballSpeed, paddle, paddle2)
    if over:
        running = False
    # Fill the window with a color (e.g., white)
    window.fill((0, 0, 0))
    for sprite in Sprite.spritesArray:
        window.blit(sprite.image, sprite.rect)
    # Update the display
    pygame.time.delay(3)
    pygame.display.flip()

# Quit Pygame
pygame.quit()
