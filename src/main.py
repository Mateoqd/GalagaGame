import pygame
import os
from game.player import Player
from game.enemy import Enemy

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Galaga Game")

# Cargar imagen de fondo
background = pygame.image.load(os.path.join("assets", "images", "background.png"))
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Crear el jugador
player = Player()

# Crear grupo de sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Crear grupo de enemigos
enemies = pygame.sprite.Group()
for _ in range(5):  # Generar 5 enemigos
    enemies.add(Enemy())

# Reloj para controlar FPS
clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Actualizar objetos
    all_sprites.update()
    player.bullets.update()
    enemies.update()

    # Dibujar en pantalla
    screen.blit(background, (0, 0))  # Fondo
    all_sprites.draw(screen)  # Jugador
    player.bullets.draw(screen)  # Balas
    enemies.draw(screen)  # Enemigos

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del juego
    clock.tick(60)

# Salir del juego
pygame.quit()
