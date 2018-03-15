# Author : Niroshiman
# Descri : Code that generates creates a circle sprite that revolves around an origin
# Instru : 1) Require pygame module

import pygame
from pygame.sprite import Group
import sys

import program_functions as pf

# RGB colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

def run_game():

	pygame.init()

	# Set screen width and height 255
	size = (800,650)
	screen = pygame.display.set_mode(size)


	pygame.display.set_caption('Spinner')

	# Create object
	discs = Group()


	clock = pygame.time.Clock()

	while True:
		# --- Main event loop

		# --- Game logic


		# --- Clearing the screen
		screen.fill(WHITE)

		# --- Update the game
		pf.check_events(screen)

		pf.create_discs(screen,discs)
		pf.update_discs(screen,discs)
		discs.draw(screen)

		# --- Updating the screen
		pygame.display.flip()


		# --- Limit to 60 FPS
		clock.tick(60)

run_game()