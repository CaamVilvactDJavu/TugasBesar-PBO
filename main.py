from pygame.locals import *
from .bintang import bintang
import pygame
import os
import random
import time
import sys
import math


def main():
    menuExit = False
    gameOverScreen = False
    gameOver = False
    bossStage = False
    stageStart = False

    menuselect = -1
    menuhighlight = 0

    wavecounter = 0
    wave = 0

    bntgjth1 = bintang(1, white, 50, 5)

    bullets = pygame.sprite.Group()
    enemybullets = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    drones = pygame.sprite.Group()
    saucers = pygame.sprite.Group()
    healthpacks = pygame.sprite.Group()

    peluru.containers = bullets
    pelurumusuh.containers = enemybullets
    musuh.containers = enemies
    ledakan.containers = explosions
    enemydrone.containers = drones
    enemysaucer.containers = saucers
    kotaksehat.containers = healthpacks

    user = player()
    pygame.display.set_caption('GalaxyWars')
    bg_music = pygame.mixer.Sound('Sprites/bg_music1.ogg')
    boss_music = pygame.mixer.Sound('Sprites/boss_music.ogg')

    (logoimage, logorect) = load_image('gamelogo1.png', -1, -1, -1)
    logorect.left = width / 2 - logorect.width / 2
    logorect.top = height / 2 - logorect.height * 5 / 4

    bg, bgrect = load_image('bg5.png')
