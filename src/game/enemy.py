import pygame
import random

# Clase del enemigo
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/images/enemy.png")  # Asegúrate de que el archivo exista
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, 750)
        self.rect.y = random.randint(20, 100)
        self.speed = 2

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:  # Reiniciar si sale de pantalla
            self.rect.y = random.randint(20, 100)
            self.rect.x = random.randint(50, 750)
