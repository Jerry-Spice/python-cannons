import pygame, sys, random, math
import time as TIME

OFFSETX = 300
OFFSETY = 550
globaltime = 0

class Cannon():
	def __init__(self, x, y, angle):
		self.x = x + OFFSETX
		self.y = y + OFFSETY
		self.angle = angle
		self.body = pygame.Surface((30,30))
		self.body.fill((150,150,150))
		self.shots = []

	def shoot(self, velocity):
		self.shots.append(Shot(self.x, self.y, self.angle, velocity))

	def display(self, screen):
		screen.blit(self.body, (self.x-30, self.y-30))

class Shot():
	def __init__(self, x, y, angle, velocity):
		self.x = x
		self.y = y
		self.startX = x
		self.startY = y
		self.angle = angle
		self.gravity = 9.8
		self.velocity = velocity
		self.body = pygame.Surface((10,10))
		self.body.fill((255,0,0))

	def updatePosition(self, time):
		self.y = (9.8*time*time)/2+math.sin(self.angle)*(self.velocity)*time+self.y
		self.x = self.x+math.cos(self.angle)*(self.velocity)
		print(self.y)

	def display(self, screen):
		screen.blit(self.body, (self.x-10, self.y-10))


pygame.init()

screen = pygame.display.set_mode((1000,600))
ground = pygame.Surface((1000,50))


cannon1 = Cannon(0,0,math.radians(-90))
cannon1.shoot(100)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	#ground stuff
	screen.fill((30,190,230))
	ground.fill((30,230,100))
	screen.blit(ground, (0,OFFSETY))


	#cannon stuff
	cannon1.display(screen)

	for i in cannon1.shots:
		if i.y <= OFFSETY:
			i.updatePosition(globaltime)
		i.display(screen)
	


	globaltime+= 0.001
	pygame.display.flip()