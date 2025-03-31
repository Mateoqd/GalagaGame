import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Ruta correcta para la imagen
        image_path = os.path.join("assets", "images", "player.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))  # Ajustamos el tamaño

        self.rect = self.image.get_rect()
        self.rect.center = (400, 500)  # Posición inicial

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < 800:
            self.rect.x += 5

from game.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Código de inicialización de la nave...

        self.bullets = pygame.sprite.Group()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:  # Disparar con la barra espaciadora
            bullet = Bullet(self.rect.centerx, self.rect.top)
            self.bullets.add(bullet)

        self.bullets.update()
