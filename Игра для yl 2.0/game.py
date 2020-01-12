import pygame


pygame.init()
window = pygame.display.set_mode((1024, 1024))  # создаем окно
pygame.display.set_caption('Game for YL')  # добавляем имя игры
bg = pygame.image.load('background.png')
player_1 = pygame.image.load('rocket_1.png')
player_2 = pygame.image.load('rocket_2.png')
font = pygame.font.SysFont("comicsans", 30, True)


class Bullet:
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.velosity = 8 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)



class Player(object):
    def __init__(self, x, y, width, height, pic):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.pic = pic
        self.vel = 5
        self.hp = 500

    def draw(self, window):
        window.blit(self.pic, (self.x, self.y))


def draw_window():
    window.blit(bg, (0, 0))
    hero_1.draw(window)
    hero_2.draw(window)

    hp_1 = font.render("PLAYER 1 HP: " + str(hero_1.hp), 1, (255, 255, 255))
    window.blit(hp_1, (8, 10))

    hp_2 = font.render("PLAYER 2 HP: " + str(hero_2.hp), 1, (255, 255, 255))
    window.blit(hp_2, (810, 10))

    for bullet in bullets:
        bullet.draw(window)
    pygame.display.update()


hero_1 = Player(200, 500, 200, 200, player_1)
hero_2 = Player(800, 500, 200, 200, player_2)
bullets = []
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # если нажать крестик игра завершается без ошибки
            run = False

    for bullet in bullets:
        if bullet.x < 1024 and bullet.x > 0:
            bullet.x += bullet.velosity
        else:
            bullets.pop(bullets.index(bullet))
        if hero_1.x < bullet.x < hero_1.x + 100 and hero_1.y < bullet.y < hero_1.y + 100:
            hero_1.hp -= 2

        if hero_2.x < bullet.x < hero_2.x + 100 and hero_2.y < bullet.y < hero_2.y + 100:
            hero_2.hp -= 2

    keys = pygame.key.get_pressed()  # все клавиши

    if keys[pygame.K_SPACE]:
        if len(bullets) < 50:
            bullets.append(Bullet(round(hero_1.x + 110), round(hero_1.y +
            60), 5, (255, 0, 0), 1))

    if keys[pygame.K_RETURN]:
        if len(bullets) < 50:
            bullets.append(Bullet(round(hero_2.x - 10), round(hero_2.y +
            47), 5, (0, 0, 255), -1))

    if keys[pygame.K_a] and hero_1.x > hero_1.vel + 5:  # двжение влево
        hero_1.x -= hero_1.vel

    if keys[pygame.K_d] and hero_1.x < 1024 - hero_1.width - 10:  # двжение вправо
        hero_1.x += hero_1.vel

    if keys[pygame.K_w] and hero_1.y > hero_1.vel + 5:  # двжение вверх
        hero_1.y -= hero_1.vel

    if keys[pygame.K_s] and hero_1.y < 1080 - hero_1.height - 10:  # движение вниз
        hero_1.y += hero_1.vel

    if keys[pygame.K_LEFT] and hero_2.x > hero_2.vel + 5:  # двжение влево
        hero_2.x -= hero_2.vel

    if keys[pygame.K_RIGHT] and hero_1.x < 1024 - hero_1.width - 10:  # двжение вправо
        hero_2.x += hero_2.vel

    if keys[pygame.K_UP] and hero_2.y > hero_2.vel + 5:  # двжение вверх
        hero_2.y -= hero_2.vel

    if keys[pygame.K_DOWN] and hero_2.y < 1080 - hero_2.height - 10:  # движение вниз
        hero_2.y += hero_2.vel

    draw_window()

pygame.quit()
