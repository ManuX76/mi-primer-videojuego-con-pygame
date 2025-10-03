import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Beat Them Up - Rectángulos")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 128, 255)
ENEMY_COLOR = (255, 0, 0)
BG_COLOR = (50, 50, 50)

# Jugador
player = pygame.Rect(100, HEIGHT - 150, 50, 100)
player_speed = 5

# Enemigos
enemy_list = [pygame.Rect(random.randint(400, WIDTH - 50), HEIGHT - 150, 50, 100) for _ in range(3)]
enemy_speed = 2

# Pantalla de inicio
def show_start_screen():
    screen.fill(BG_COLOR)
    font = pygame.font.SysFont(None, 60)
    title_text = font.render("Beat Them Up", True, WHITE)
    start_text = pygame.font.SysFont(None, 40).render("Presiona cualquier tecla para comenzar", True, WHITE)
    screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 3))
    screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    wait_for_key()

# Esperar a que el jugador presione una tecla
def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Pantalla de juego
def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(60)
        screen.fill(BG_COLOR)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.x -= player_speed
        if keys[pygame.K_RIGHT]:
            player.x += player_speed

        # Movimiento de enemigos
        for enemy in enemy_list:
            if enemy.x > player.x:
                enemy.x -= enemy_speed
            elif enemy.x < player.x:
                enemy.x += enemy_speed

        # Dibujar jugador y enemigos
        pygame.draw.rect(screen, PLAYER_COLOR, player)
        for enemy in enemy_list:
            pygame.draw.rect(screen, ENEMY_COLOR, enemy)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Ejecutar juego
show_start_screen()