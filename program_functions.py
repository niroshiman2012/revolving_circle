# Author : Niroshiman
import sys
import pygame

from disc import Disc

def check_events(screen):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

def create_discs(screen,discs):
	"""Create discs and place it on the screen."""
	if len(discs) < 1:
		disc = Disc(screen)
		discs.add(disc)

def update_discs(screen,discs):
	"""Update position of the discs."""
	discs.update()




