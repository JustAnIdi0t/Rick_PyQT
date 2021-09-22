import pygame, sys, random

def draw_back():
    screen.blit(back_g, (0,0))
    
def draw_char():
    screen.blit(character, char_rect)
    screen.blit(meteor, met_rect)
    screen.blit(meteor2, met_rect2)
    screen.blit(meteor3, met_rect3)
    screen.blit(flag, flag_rect)
    
def collisions():
    if char_rect.colliderect(met_rect) or char_rect.colliderect(met_rect2) or char_rect.colliderect(met_rect3):
        pygame.quit()
        sys.exit()
    if char_rect.colliderect(flag_rect):
        pygame.quit()
        sys.exit()
        print('You win')

pygame.init()
screen = pygame.display.set_mode((1700,1000))
clock = pygame.time.Clock()

randx = random.randint(300, 1700)
randy = random.randint(1, 600)
randx2 = random.randint(300, 1700)
randy2 = random.randint(1, 600)
randx3 = random.randint(300, 1700)
randy3 = random.randint(1, 600)
randx4 = random.randint(300, 1700)
randy4 = random.randint(1, 600)

dir1 = random.randint(-50, 50)
dir2 = random.randint(-34, 5)
dir3 = random.randint(-9, 45)
dir4 = random.randint(-78, 23)
dir5 = random.randint(-7, 50)
dir6 = random.randint(-32, 50)
dir7 = random.randint(-98, 98)
dir8 = random.randint(-12, 50)

back_g = pygame.image.load('Background.png').convert()
character = pygame.image.load('Person.png').convert()
char_rect = character.get_rect(center = (200, 770))
meteor = pygame.image.load('Meteor.png').convert()
met_rect = meteor.get_rect(center = (randx, randy))
meteor2 = pygame.image.load('B_met.png').convert()
met_rect2 = meteor2.get_rect(center = (randx2, randy2))
meteor3 = pygame.image.load('G_met.png').convert()
met_rect3 = meteor3.get_rect(center = (randx3, randy3))
flag = pygame.image.load('Flag.png').convert()
flag_rect = flag.get_rect(center = (randx4, randy4))

    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                char_rect.move_ip(25, 0)
                met_rect.move_ip(dir1, dir2)
                met_rect2.move_ip(dir8, dir4)
                met_rect3.move_ip(dir3, dir5)
            if event.key == pygame.K_LEFT:
                char_rect.move_ip(-25, 0)
                met_rect.move_ip(dir3, dir6)
                met_rect2.move_ip(dir7, dir7)
                met_rect3.move_ip(dir3, dir2)
            if event.key == pygame.K_UP:
                char_rect.move_ip(0, -25)
                met_rect.move_ip(dir1, dir1)
                met_rect2.move_ip(dir4, dir8)
                met_rect3.move_ip(dir1, dir6)
            if event.key == pygame.K_DOWN:
                char_rect.move_ip(0, 25)
                met_rect.move_ip(dir3, dir8)
                met_rect2.move_ip(dir8, dir8)
                met_rect3.move_ip(dir2, dir1)
                
            
    def main():
        pygame.display.set_caption('Meteor dodger')
        draw_back()
        draw_char()
        collisions()
        
        pygame.display.update()
        clock.tick(90)
        
    main()
    
    pygame.display.update()
    clock.tick(90)
    
