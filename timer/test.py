import pygame
from time import sleep
def bells(soundfile, max_time):		
	pygame.init()
	sfx = pygame.mixer.Sound(soundfile)
	sfx.play(maxtime=max_time)

bells("tinsha.wav", 12000)	
sleep(13)