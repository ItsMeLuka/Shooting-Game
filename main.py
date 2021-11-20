import pygame as pg


pg.init()

screen_width = 800
screen_height = int(screen_width * 0.8)

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Shooter')

#set framerate
clock = pg.time.Clock()
fps = 60


#define player action variables
moving_left = False
moving_right = False

#define colors
BG = (144, 201, 120)

def draw_bg():
    screen.fill(BG)


class Soldier(pg.sprite.Sprite):
    def __init__(self,  char_type,  x, y, scale, speed):
        pg.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pg.image.load(f'img/{self.char_type}/Idle/0.png')
        self.image = pg.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, moving_left, moving_right):
        #reset movement variables
        dx = 0
        dy = 0
        #assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        #update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(pg.transform.flip(self.image, self.flip, False), self.rect)

player = Soldier('player', 200, 200, 3, 5)
enemy = Soldier('enemy', 400, 200, 3, 5)


run = True
while run:

    clock.tick(fps)
    draw_bg()

    player.draw()
    enemy.draw()
    player.update(moving_left, moving_right)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a:
                moving_left = True
            if event.key == pg.K_d:
                moving_right = True
            if event.key == pg.K_ESCAPE:
                run = False


        #keyboard button released
        if event.type == pg.KEYUP:
            if event.key == pg.K_a:
                moving_left = False
            if event.key == pg.K_d:
                moving_right = False

    
    pg.display.update()

pg.quit()
