import pygame
import os
import math
import random
pygame.font.init()
pygame.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Falcon Wing - TEAMANGG!")

# Load images
RED_ENEMY = pygame.transform.scale(pygame.image.load(os.path.join("assets", "red.png")), (100, 100))
GREEN_ENEMY = pygame.transform.scale(pygame.image.load(os.path.join("assets", "green.png")), (100, 100))
YELLOW_ENEMY = pygame.transform.scale(pygame.image.load(os.path.join("assets", "yellow.png")), (100, 100))

# Player image
FALCON = pygame.transform.scale(pygame.image.load(os.path.join("assets", "Falcon.png")), (100, 100))

# Projectiles
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))
FEATHER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "7.png")).convert(), (WIDTH, 750))
#For scrolling
bg_height = BG.get_height()
tiles = math.ceil(HEIGHT/bg_height) + 1
print(tiles)
scroll  = 0
class Laser:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y += vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(self, obj)


class Ship:
    COOLDOWN = 30

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            elif laser.collision(obj):
                obj.health -= 10
                self.lasers.remove(laser)

    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = FALCON
        self.laser_img = FEATHER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)

    def healthbar(self, window):
        pygame.draw.rect(window, (255,255,255), (self.x, self.y + self.ship_img.get_height() + 10 , self.ship_img.get_width(), 15))
        pygame.draw.rect(window, (255,0,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))


class Enemy(Ship):
    COLOR_MAP = {
                "red": (RED_ENEMY, RED_LASER),
                "green": (GREEN_ENEMY, GREEN_LASER),
                "yellow": (YELLOW_ENEMY, YELLOW_LASER)
                }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel

    def shoot(self):
        if self.cool_down_counter == 0:
            laser = Laser(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.cool_down_counter = 1


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    main_font = pygame.font.Font("assets/font.ttf", 20)
    tutorial_font = pygame.font.Font("assets/font.ttf", 10)
    lost_font = pygame.font.Font("assets/font.ttf", 20)

    enemies = []
    wave_length = 5
    enemy_vel = 1

    player_vel = 5
    laser_vel = 10

    player = Player(300, 630)

    clock = pygame.time.Clock()

    lost = False
    lost_count = 0

    def redraw_window():
        global scroll, tiles
        for i in range(0, 2):
            WIN.blit(BG, (0, i * bg_height + scroll))
        scroll += 5
        if scroll >= bg_height:
            scroll = 0
        bg_y = scroll % bg_height
    
        # Blit the background image at the correct position
        WIN.blit(BG, (0, bg_y))
        WIN.blit(BG, (0, bg_y - bg_height))

        # draw text
        lives_label = main_font.render(f"Lives: {lives}", 1, (255,255,255))
        level_label = main_font.render(f"Level: {level}", 1, (255,255,255))
        tut_label = tutorial_font.render(f"Controls:", 1,(255,255,255))
        tut_label1 = tutorial_font.render(f"Movement: W, A, S, D", 1,(255,255,255))
        tut_label2 = tutorial_font.render(f"Shoot: Space", 1,(255,255,255))
        tut_label3 = tutorial_font.render(f"Objective:", 1,(255,255,255))
        tut_label4 = tutorial_font.render(f"Don't let the Virus pass!", 1,(255,255,255))
        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))
        WIN.blit(tut_label, (WIDTH - tut_label.get_width() - 10, 35))
        WIN.blit(tut_label1, (WIDTH - tut_label1.get_width() - 10, 50))
        WIN.blit(tut_label2, (WIDTH - tut_label2.get_width() - 10, 65))
        WIN.blit(tut_label3, (10, 35))
        WIN.blit(tut_label4, (10, 50))
        for enemy in enemies:
            enemy.draw(WIN)

        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("You Lost!!", 1, (255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 350))
        pygame.display.update()

    while run:
        clock.tick(FPS)
       
        redraw_window()


        if player.health <= 0:
            lives -= 1
            player.health = 100
        elif lives <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                main_menu

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "yellow", "green"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_vel > 0: # left
            player.x -= player_vel
        if keys[pygame.K_d] and player.x + player_vel + player.get_width() < WIDTH: # right
            player.x += player_vel
        if keys[pygame.K_w] and player.y - player_vel > 0: # up
            player.y -= player_vel
        if keys[pygame.K_s] and player.y + player_vel + player.get_height() + 15 < HEIGHT: # down
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()

        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel, player)

            if random.randrange(0, 2*60) == 1:
                enemy.shoot()

            if collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)

        player.move_lasers(-laser_vel, enemies)
  

def main_menu():
    title_font = pygame.font.Font("assets/font.ttf", 25)
    run = True
    while run:
        WIN.blit(BG, (0,0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255,255,255))
        WIN.blit(title_label, (WIDTH/2 - title_label.get_width()/2, 350))
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()


main_menu()