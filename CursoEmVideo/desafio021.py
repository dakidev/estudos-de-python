'''
Tocar .mp3 pelo python
'''

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('./ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
#input('Agora você escuta?')
while(pygame.mixer.music.get_busy()): pass
#pygame.event.wait()