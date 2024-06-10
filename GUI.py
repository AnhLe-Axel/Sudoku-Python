import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("fonts/CookieCrisp-L36ly.ttf", 50)

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()
text_surface = test_font.render("My game", False, (64,64,64))
text_rect = text_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/fly1.png').convert_alpha()
snail_surface = pygame.transform.scale_by(snail_surface, 0.1)
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surface = pygame.image.load('graphics/archer.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,320))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                if player_rect.bottom == 320:
                    player_gravity = -20
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rect.bottom == 320:
                    player_gravity = -20

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, "#c0e8ec", text_rect)
    screen.blit(text_surface, text_rect)

    snail_rect.left -= 4
    if snail_rect.right < 0: snail_rect.left = 800
    pygame.draw.rect(screen, "Red", snail_rect, 2)
    screen.blit(snail_surface, snail_rect)

    # Player
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom > 320: player_rect.bottom = 320
    pygame.draw.rect(screen, "Green", player_rect, 2)
    screen.blit(player_surface, player_rect)

    # Collision
    if snail_rect.colliderect(player_rect):
        pygame.quit()
        exit()

    pygame.display.update()
    clock.tick(60)