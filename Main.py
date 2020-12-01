import pygame, random, time, pygame.event

from Player import *
from Bullet import *
from Spider import *
from Bomb import *
from Centipede import *
from Boom import *
from Scorpion import *
from Fleas import *

pygame.init()
bg = (25, 25, 25)
level = 1
game_map = []
empty = pygame.Surface([20, 20])
empty.fill(bg)
mushroom_image = pygame.image.load('msh1.png')
mushroom_image2 = pygame.image.load('msh2.png')
mushroom_image3 = pygame.image.load('msh3.png')
mushroom_image.set_colorkey((0, 0, 0))
mushroom_image2.set_colorkey((0, 0, 0))
mushroom_image3.set_colorkey((0, 0, 0))


###PREPARE YOUR AXIS
def setup_the_map_of_the_game():
    global game_map
    game_map = []
    for x in range(40):
        arrayOfZeros = [0] * 30
        game_map.append(arrayOfZeros)
    for x in range(30):
        randomX = random.randint(0, 29)
        randomY = random.randint(0, 27)
        game_map[randomX][randomY] = 1



def draw_the_map_of_the_game():
    for column in range(30):
        for row in range(40):
            spot = game_map[row][column]
            if spot == 1:
                screen.blit(empty, [column * 20, row * 20])
                screen.blit(mushroom_image, [column * 20, row * 20])
            if spot == 2:
                screen.blit(empty, [column * 20, row * 20])
                screen.blit(mushroom_image2, [column * 20, row * 20])
            if spot == 3:
                screen.blit(empty, [column * 20, row * 20])
                screen.blit(mushroom_image3, [column * 20, row * 20])
            if spot == 4:
                screen.blit(empty, [column * 20, row * 20])
                game_map[row][column] = 0


def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            return event.key
        else:
            pass


size = [600, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Centipede")

player = Player(300, 700)
bullet = Bullet()
bomb = Bomb()
fleas = Fleas()
bulletGroup = pygame.sprite.Group()
bulletGroup.add(bullet)
clock = pygame.time.Clock() # Setup the clock for a decent framerate
going = True
# Drawing background
background = pygame.Surface(size)
background.fill(bg)
screen.blit(background, (0, 0))

allsprites = pygame.sprite.Group()
allsprites.add(player)
allsprites.add(bulletGroup)
allsprites.add(bomb)
allsprites.add(fleas)
booms = pygame.sprite.Group()

# Create THE ALMIGHTY
centis = pygame.sprite.Group()
for m in range(12):
    centi = Centipede(20 * m, -20)
    centis.add(centi)

spider = Spider()
allsprites.add(spider)
allsprites.add(centis)
allsprites.add(booms)
# spider.activate()
# bomb.activate()
# Program Loop!!
setup_the_map_of_the_game()
clock_tick = 20
game_mode = 'menu'
tickCounter = 0

scorpion = Scorpion()
allsprites.add(spider)
allsprites.add(scorpion)
allsprites.add(centis)
allsprites.add(booms)
# spider.activate()
# bomb.activate()
# Program Loop!!
setup_the_map_of_the_game()
clock_tick = 20
game_mode = 'menu'
tickCounter = 0

# FONTS------------------
gameOverFont = pygame.font.Font('ARDARLING.ttf', 70)
clickToStart = pygame.font.Font('ARDARLING.ttf', 40)
highScore = pygame.font.Font('ARDARLING.ttf', 50)
# -----------------------
# MENU IMAGES
# 0 centi
# 200 play
# 325 high
# 425 ins
# 525 quit
# 700 footer
menu_header = []
menu_header.append(pygame.image.load("CentipedeMenu1.png"))
menu_header.append(pygame.image.load("CentipedeMenu2.png"))
menu_high = []
menu_high.append(pygame.image.load("MenuH1.png"))
menu_high.append(pygame.image.load("MenuH2.png"))
menu_ins = []
menu_ins.append(pygame.image.load("MenuIns1.png"))
menu_ins.append(pygame.image.load("MenuIns2.png"))
menu_play = []
menu_play.append(pygame.image.load("MenuPlay1.png"))
menu_play.append(pygame.image.load("MenuPlay2.png"))
menu_quit = []
menu_quit.append(pygame.image.load("MenuQ1.png"))
menu_quit.append(pygame.image.load("MenuQ2.png"))
menu_footer = pygame.image.load("MenuFooter.png")
# INSTRUCTIONS IMAGES
inst_space = []
for i in range(1, 5):
    inst_space.append(pygame.image.load("inst%d.png" % i))
inst_up = []
for i in range(1, 5):
    inst_up.append(pygame.image.load("instup%d.png" % i))
inst_shroom = []
for i in range(1, 7):
    inst_shroom.append(pygame.image.load("instshroom%d.png" % i))
inst_bomb = []
for i in range(1, 5):
    inst_bomb.append(pygame.image.load("instbomb%d.png" % i))
inst_spider = []
for i in range(1, 5):
    inst_spider.append(pygame.image.load("instspider%d.png" % i))
inst_scorpion = []
for i in range(1, 5):
    inst_scorpion.append(pygame.image.load("Scorpion%d.png" % i))

inst_centi = []
for i in range(1, 5):
    inst_centi.append(pygame.image.load("instcenti%d.png" % i))
inst_footer = pygame.image.load("ins_footer2.png")
high_footer = pygame.image.load("HighFooter.png")

playerNames = ['111', '222', '333', '444', '555', '666', '777', '888', '999']
playerScores = [999, 888, 777, 666, 555, 444, 333, 22, 1]
# playerScores[1:0]=[12]
currentUser = ['e', 'l', 'f']
currentCharacter = 0
currentScore = 0
lastScore = 0

menu_selection = 1
slowDownAnimation = 0
while going:
    clock.tick(clock_tick)
    tickCounter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            going = False
    if game_mode == 'savescore':
        lastScore = currentScore
        currentCharacter = 0
        userText = ''
        for i in range(len(currentUser)):
            userText += currentUser[i]
        text = gameOverFont.render(userText, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        screen.blit(text, [text_x, text_y + 300])
        pygame.display.flip()
        while currentCharacter < 3:
            inkey = get_key()
            if inkey == pygame.K_RETURN:
                game_mode = 'menu'
                break
            userText = ''
            if inkey == pygame.K_BACKSPACE:
                currentUser = currentUser[0:-1]
            elif inkey <= 127:
                currentUser[currentCharacter] = chr(inkey - 32)
                currentCharacter += 1

                for i in range(len(currentUser)):
                    userText += currentUser[i]

                text = gameOverFont.render(userText, True, (255, 255, 255))
                text_rect = text.get_rect()
                text_x = screen.get_width() / 2 - text_rect.width / 2
                refresh = pygame.Surface([text_rect.width, text_rect.height])
                refresh.fill(bg)
                screen.blit(refresh, [text_x, text_y + 300])
                screen.blit(text, [text_x, text_y + 300])
                pygame.display.flip()

        print('name done')
        ##        if lastScore>=playerScores[0]:
        ##            playerScores[0:0]=[lastScore]
        print(lastScore)
        print(userText)
        for i in range(9):
            if lastScore >= playerScores[i]:
                ##                playerScores[9].remove()
                playerScores.insert(i, lastScore)
                playerNames.insert(i, userText)
                print(userText)
                break
        game_mode = 'menu'
    if game_mode == 'high':
        pygame.display.set_caption("Centipede Game")
        # ITEMS ON THE MIDDLE
        title = gameOverFont.render('High Scores', True, (255, 255, 255))
        screen.blit(high_footer, (0, 719))

        # LEFT SIDE OF SCREEN
        title_rect = title.get_rect()
        title_x = screen.get_width() / 2 - title_rect.width / 2
        title_y = 40
        screen.blit(title, [title_x, title_y])
        for i in range(9):
            name = highScore.render(str(i + 1) + '. ' + playerNames[i], True, (255, 255, 255))
            text_rect = name.get_rect()
            name_x = screen.get_width() / 4 - text_rect.width / 2
            name_y = 150 + 60 * (i)
            screen.blit(name, [name_x, name_y])

        # RIGHT SIDE OF SCREEN
        for i in range(9):
            name = highScore.render(str(playerScores[i]), True, (255, 255, 255))
            text_rect = name.get_rect()
            name_x = 3 * (screen.get_width() / 4) - text_rect.width / 2
            name_y = 150 + 60 * (i)
            screen.blit(name, [name_x, name_y])
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_ESCAPE]):
            game_mode = 'menu'
            refresh = pygame.Surface([600, 800])
            refresh.fill(bg)
            screen.blit(refresh, [0, 0])
            menu_selection = 2

    if game_mode == 'inst':
        pygame.display.set_caption("Centipede")
        if (tickCounter % 10 == 0):
            slowDownAnimation += 1
            screen.blit(inst_footer, (0, 600))
            screen.blit(inst_space[slowDownAnimation % 4], (0, 0))
            screen.blit(inst_up[slowDownAnimation % 4], (300, 0))
            screen.blit(inst_shroom[slowDownAnimation % 6], (0, 200))
            screen.blit(inst_bomb[slowDownAnimation % 4], (300, 200))
            screen.blit(inst_spider[slowDownAnimation % 4], (0, 400))
            screen.blit(inst_scorpion[slowDownAnimation % 4], (300, 400))
            screen.blit(inst_centi[slowDownAnimation % 4], (300, 600))
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_ESCAPE]):
            game_mode = 'menu'
            refresh = pygame.Surface([600, 800])
            refresh.fill(bg)
            screen.blit(refresh, [0, 0])
            menu_selection = 3

            slowDownAnimation = 0

    if game_mode == 'menu':
        pygame.display.set_caption("Centipede")
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_DOWN] and menu_selection < 4):
            menu_selection += 1

        if (keys[pygame.K_UP] and menu_selection > 1):
            menu_selection -= 1

        screen.blit(menu_header[tickCounter % 2], (0, 0))
        screen.blit(menu_footer, (0, 625))
        if menu_selection == 1:
            screen.blit(menu_play[1], (0, 200))
        else:
            screen.blit(menu_play[0], (0, 200))

        if menu_selection == 2:
            screen.blit(menu_high[1], (0, 325))
        else:
            screen.blit(menu_high[0], (0, 325))

        if menu_selection == 3:
            screen.blit(menu_ins[1], (0, 425))
        else:
            screen.blit(menu_ins[0], (0, 425))

        if menu_selection == 4:
            screen.blit(menu_quit[1], (0, 525))
        else:
            screen.blit(menu_quit[0], (0, 525))

        if (keys[pygame.K_RETURN]):
            refresh = pygame.Surface([600, 700])
            refresh.fill(bg)
            screen.blit(refresh, [0, 0])
            if menu_selection == 1:
                game_mode = 'play'
            elif menu_selection == 2:
                game_mode = 'high'
            elif menu_selection == 3:
                game_mode = 'inst'
            elif menu_selection == 4:
                going = False
    elif game_mode == 'gameover':

        ##        global lastScore
        lastScore = currentScore
        ##        currentScore=0

        text = gameOverFont.render("GAME OVER!", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y - 200])

        text = clickToStart.render("Hit [S] to Save", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        screen.blit(text, [text_x, text_y + 210])

        text = clickToStart.render("Hit Enter to Start Again", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        screen.blit(text, [text_x, text_y + 90])

        text = clickToStart.render("Hit Escape for Menu", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        screen.blit(text, [text_x, text_y + 150])

        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RETURN]):
            game_mode = 'play'
            refresh = pygame.Surface([600, 700])
            refresh.fill(bg)
            screen.blit(refresh, [0, 0])

            centis = pygame.sprite.Group()
            for m in range(12):
                centi = Centipede(20 * m, -20)
                centis.add(centi)
                setup_the_map_of_the_game()
                allsprites.add(centis)
            allsprites = pygame.sprite.Group()
            allsprites.add(player)
            allsprites.add(bulletGroup)
            allsprites.add(bomb)
            allsprites.add(fleas)
            allsprites.add(spider)
            allsprites.add(scorpion)
            allsprites.add(centis)
            allsprites.add(booms)
            spider.deactivate()
            scorpion.deactivate()
            bomb.deactivate()
            bullet.deactivate()
            fleas.deactivate()
        if (keys[pygame.K_ESCAPE]):
            game_mode = 'menu'
            refresh = pygame.Surface([600, 700])
            refresh.fill(bg)
            screen.blit(refresh, [0, 0])

            centis = pygame.sprite.Group()
            for m in range(12):
                centi = Centipede(20 * m, -20)
                centis.add(centi)
                setup_the_map_of_the_game()
                allsprites.add(centis)
            allsprites = pygame.sprite.Group()
            allsprites.add(player)
            allsprites.add(bulletGroup)
            allsprites.add(bomb)
            allsprites.add(fleas)
            allsprites.add(spider)
            allsprites.add(scorpion)
            allsprites.add(centis)
            allsprites.add(booms)
            spider.deactivate()
            scorpion.deactivate()
            bomb.deactivate()
            fleas.deactivate()
            bullet.deactivate()
            menu_selection = 1

        if (keys[pygame.K_s]):
            game_mode = 'savescore'

            centis = pygame.sprite.Group()
            for m in range(12):
                centi = Centipede(20 * m, -20)
                centis.add(centi)
                setup_the_map_of_the_game()
                allsprites.add(centis)
            allsprites = pygame.sprite.Group()
            allsprites.add(player)
            allsprites.add(bulletGroup)
            allsprites.add(bomb)
            allsprites.add(spider)
            allsprites.add(scorpion)
            allsprites.add(centis)
            allsprites.add(fleas)
            allsprites.add(booms)
            spider.deactivate()
            scorpion.deactivate()
            bomb.deactivate()
            fleas.deactivate()
            bullet.deactivate()
    if game_mode == 'play':
        shootTileX = int(bullet.x / 20)
        shootTileY = int(bullet.y / 20)
        # Bullet
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_SPACE] and bullet.canBullet):
            bullet.activate(player.rect.x + 8, player.rect.y + 6)
        for c in centis:
            if c.left_right == 1 and c.rect.x < 580:
                if game_map[int(c.rect.y / 20)][int(c.rect.x / 20) + 1]:
                    c.collide()
            else:
                if game_map[int(c.rect.y / 20)][int(c.rect.x / 20) - 1]:
                    c.collide()

            if c.rect.x == bullet.rect.x - 8 and c.rect.y == bullet.rect.y - 6:
                c.kill()
                game_map[shootTileY - 1][shootTileX] = 1
                currentScore += 10
                bullet.deactivate()

        if game_map[shootTileY - 1][shootTileX] > 0:
            game_map[shootTileY - 1][shootTileX] = game_map[shootTileY - 1][shootTileX] + 1
            currentScore += 3
            bullet.deactivate()


        if spider.isActive == 0:
            rnd = random.randint(0, 500 / level)
            if rnd == 0:
                spider.activate()

        if pygame.sprite.spritecollide(spider, bulletGroup, False):
            boom = Boom(spider.rect.x, spider.rect.y)
            allsprites.add(boom)
            booms.add(boom)
            spider.deactivate()
            bullet.deactivate()
            currentScore += 50

        if scorpion.isActive == 0:
            rnd = random.randint(0, 500 / level)
            if rnd == 0:
                scorpion.activate()

        if pygame.sprite.spritecollide(scorpion, bulletGroup, False):
            boom = Boom(scorpion.rect.x, scorpion.rect.y)
            allsprites.add(boom)
            booms.add(boom)
            scorpion.deactivate()
            bullet.deactivate()
            currentScore += 50


        if bomb.isActive == 0:
            rnd = random.randint(0, 10 / level)
            if rnd == 0:
                bomb.activate()
        else:
            if (bomb.drop):
                rnd = random.randint(1, 5)

                if (rnd == 1 and bomb.ay > 0 and bomb.isActive):

                    game_map[int(bomb.ay / 20) + 1][int(bomb.ax / 20)] = 1
                    bomb.drop = 0

        if pygame.sprite.spritecollide(bomb, bulletGroup, False):
            boom = Boom(bomb.rect.x, bomb.rect.y)
            allsprites.add(boom)
            booms.add(boom)
            bomb.deactivate()
            bullet.deactivate()
            currentScore += 30

        if fleas.isActive == 0:
            rnd = random.randint(0, 10 / level)
            if rnd == 0:
                fleas.activate()
        else:
            if (fleas.drop):
                rnd = random.randint(1, 5)

                if (rnd == 1 and fleas.ay > 0 and fleas.isActive):

                    game_map[int(fleas.ay / 20) + 1][int(fleas.ax / 20)] = 1
                    bomb.drop = 0

        if pygame.sprite.spritecollide(fleas, bulletGroup, False):
            boom = Boom(fleas.rect.x, fleas.rect.y)
            allsprites.add(boom)
            booms.add(boom)
            fleas.deactivate()
            bullet.deactivate()
            currentScore += 30

        # Player Collide!
        if pygame.sprite.spritecollide(player, centis, False):
            boom = Boom(player.rect.x, player.rect.y)
            allsprites.add(boom)
            booms.add(boom)
            game_mode = 'gameover'
        if pygame.sprite.collide_rect(player, spider):
            boom = Boom(player.rect.x, player.rect.y)
            allsprites.add(boom)
            booms.add(boom)
            game_mode = 'gameover'
        if pygame.sprite.collide_rect(player, bomb):
            boom = Boom(player.rect.x, player.rect.y)
            allsprites.add(boom)
            booms.add(boom)
            game_mode = 'gameover'


        if (tickCounter % 3 == 0):
            player.update(keys)
        # PLAYER SCORE
        ##        score_clear=pygame.Surface([600,800])
        ##        score_clear.fill(bg)
        ##        screen.blit(score_clear,[5,5])
        ##        score = clickToStart.render(str(currentScore), True, (255,255,255))
        ##        screen.blit(score, [5, 5])
        pygame.display.set_caption("Score : " + str(currentScore))

        allsprites.clear(screen, background)
        bullet.update()
        spider.update()
        scorpion.update()
        bomb.update()
        fleas.update()
        centis.update()
        booms.update()
        draw_the_map_of_the_game()
        allsprites.draw(screen)
    ###  centis.update()
    pygame.display.flip()
pygame.quit()