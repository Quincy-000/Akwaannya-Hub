# window_test.py
# A quick check that Pygame can open a window on this machine.

import pygame

# Start up all of Pygame's modules.
pygame.init()

# Create the window: 600 pixels wide, 600 pixels tall.
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Window test")

# This loop keeps the window open until we close it.
running = True
while running:
    # Check every event (mouse click, key press, closing the window).
    for event in pygame.event.get():
        # The X button on the window sends a QUIT event.
        if event.type == pygame.QUIT:
            running = False

    # Paint the whole window a dark blue colour (red, green, blue values).
    screen.fill((20, 30, 60))

    # Show what we just painted.
    pygame.display.flip()

# Shut Pygame down cleanly.
pygame.quit()