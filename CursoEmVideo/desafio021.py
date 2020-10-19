'''
Tocar .mp3 pelo python
'''

import pygame
pygame.mixer.init()
#pygame.init()
pygame.mixer.music.load('./ex021.wav')
pygame.mixer.music.play()
while(pygame.mixer.music.get_busy()): pass
#pygame.event.wait()