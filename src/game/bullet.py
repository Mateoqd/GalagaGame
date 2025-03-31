import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 15))
        self.image.fill((255, 255, 0))  # Color amarillo
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.rect.y -= 5  # Mover la bala hacia arriba
        if self.rect.bottom < 0:
            self.kill()  # Eliminar la bala si sale de la pantalla
