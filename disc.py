# Author : Niroshiman

import pygame
from pygame.sprite import Sprite
import math

class Disc(Sprite):
	"""A class to manage discs that spin on the screen."""

	def __init__(self,screen):
		"""Initialize the disc object."""
		super(Disc,self).__init__()
		self.screen = screen
		self.screen_rect = self.screen.get_rect()

		# Load the image of the disc and obtain its rect.
		self.image = pygame.image.load('circle.png')
		self.rect = self.image.get_rect()

		# Rect and Midpoint of screen
		self.screen_rect = self.screen.get_rect()
		self.midx,self.midy = self.screen_rect.centerx,self.screen_rect.centery

		# Spinning ball starting position
		self.radius = 220
		self.angle = float(0)
		self.rect.centerx = self.midx	# Center of rotation x coordinate
		self.rect.centery = self.midy - self.radius	# Center of rotation y coordinate
		# Increase accuracy of coordinates
		self.centery = float(self.rect.centery)
		self.centerx = float(self.rect.centerx)


	def update(self):
		"""Make the ball spin in circle using polar coordinates"""
		self.angle += 1 # degrees
		self.theta = math.radians(self.angle) # radians
		
		self.centerx = self.radius*math.cos(self.theta) + self.midx
		self.centery = self.radius*math.sin(self.theta) + self.midy

		# Update position of the circle
		self.rect.centery = self.centery
		self.rect.centerx = self.centerx





