import os
import pygame
import sys
import time
import math
import random


class bintang:

    def __init__(self, radius, warna, nofstars, cepat=5):
        self.radius = radius
        self.warna = warna
        self.cepat = cepat
        self.nofstars = nofstars
        self.posbintang = [[0 for j in range(2)] for i in range(self.nofstars)]
        for x in range(self.nofstars):
            self.posbintang[x][0] = random.randrange(0, width)
            self.posbintang[x][1] = random.randrange(0, height)

    def gambarbintang(self):
        for x in range(self.nofstars):
            pygame.draw.circle(
                screen, self.warna, (self.posbintang[x][0], self.posbintang[x][1]), self.radius)
        self.pindahbintang()

    def pindahbintang(self):
        for x in range(self.nofstars):
            self.posbintang[x][1] += self.cepat
            if self.posbintang[x][1] > height:
                self.posbintang[x][1] = 0
