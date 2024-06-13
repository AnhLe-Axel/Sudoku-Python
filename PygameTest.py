import pygame
from random import randint
from sys import exit

def display_score():
    curr_time = int((pygame.time.get_ticks() - start_time)/1000)
    score_surface = test_font.render(f'Score: {curr_time}', False, (64,64,64))
    score_rect = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rect)
    return curr_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 240:
                screen.blit(fly_surface, obstacle_rect)
            elif obstacle_rect.bottom == 320:
                screen.blit(monster_surface, obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        
        return obstacle_list
    else:
        return []

def collisions(player, obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            if player.colliderect(obstacle_rect): 
                return False
        return True
    else:
        return True

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("fonts/CookieCrisp-L36ly.ttf", 40)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

# Obstacles
fly_surface = pygame.image.load('graphics/fly1.png').convert_alpha()
fly_surface = pygame.transform.scale_by(fly_surface, 0.09)
monster_surface = pygame.image.load('graphics/monster1.png').convert_alpha()
monster_surface = pygame.transform.scale_by(monster_surface, 0.08)
obstacle_rect_list = []

# Intro screen
player_surface = pygame.image.load('graphics/archer.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,320))
player_gravity = 0
player_stand = pygame.image.load('graphics/archer.png').convert_alpha()
player_stand = pygame.transform.scale_by(player_stand, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))

instruction_surface = test_font.render(f'Press space to start the game!', False, (64,64,64))
instruction_rect = instruction_surface.get_rect(center = (400, 300))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                    if player_rect.bottom == 320:
                        player_gravity = -17
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 320:
                        player_gravity = -17
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(fly_surface.get_rect(midbottom = (randint(900, 1100),240)))
                else:
                    obstacle_rect_list.append(monster_surface.get_rect(midbottom = (randint(900, 1100),320)))
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                start_time = pygame.time.get_ticks()

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        score = display_score()

        # Player
        player_gravity += 0.8
        player_rect.y += player_gravity
        if player_rect.bottom > 320: player_rect.bottom = 320
        pygame.draw.rect(screen, "Green", player_rect, 2)
        screen.blit(player_surface, player_rect)

        #Obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #Collision
        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill((94,129,162))
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,320)
        player_gravity = 0
        score_mess = test_font.render(f'Your score: {score}', False, (64,64,64))
        score_rect = score_mess.get_rect(center = (400, 100))

        if score != 0: screen.blit(score_mess, score_rect)
        screen.blit(player_stand, player_stand_rect)
        screen.blit(instruction_surface, instruction_rect)

    pygame.display.update()
    clock.tick(60)