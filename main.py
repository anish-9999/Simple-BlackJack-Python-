import casino
import pygame
import time

pygame.init()
cardBack = pygame.image.load('cardBack.png')
screen = pygame.display.set_mode((1300, 900))
pygame.display.set_caption('Black Jack')
clock = pygame.time.Clock()
myfont = pygame.font.SysFont('monospace', 50)
smallFont = pygame.font.SysFont('monospace', 30)
screen.fill((0, 128, 0))
dec = casino.cards()
cardList = dec.getCards()
d = casino.dealer(cardList)
p = casino.player(cardList)

pygame.display.flip()

onTable = []
topCards = []

cardImg = [None]
# Load 52 Images
two_clubs = pygame.image.load('2_of_clubs.png')
two_diamonds = pygame.image.load('2_of_diamonds.png')
two_hearts = pygame.image.load('2_of_hearts.png')
two_spades = pygame.image.load('2_of_spades.png')

three_clubs = pygame.image.load('3_of_clubs.png')
three_spades = pygame.image.load('3_of_spades.png')
three_diamonds = pygame.image.load('3_of_diamonds.png')
three_hearts = pygame.image.load('3_of_hearts.png')

four_clubs = pygame.image.load('4_of_clubs.png')
four_spades = pygame.image.load('4_of_spades.png')
four_diamonds = pygame.image.load('4_of_diamonds.png')
four_hearts = pygame.image.load('4_of_hearts.png')

five_clubs = pygame.image.load('5_of_clubs.png')
five_spades = pygame.image.load('5_of_spades.png')
five_diamonds = pygame.image.load('5_of_diamonds.png')
five_hearts = pygame.image.load('5_of_hearts.png')

six_clubs = pygame.image.load('6_of_clubs.png')
six_spades = pygame.image.load('6_of_spades.png')
six_diamonds = pygame.image.load('6_of_diamonds.png')
six_hearts = pygame.image.load('6_of_hearts.png')

seven_clubs = pygame.image.load('7_of_clubs.png')
seven_spades = pygame.image.load('7_of_spades.png')
seven_diamonds = pygame.image.load('7_of_diamonds.png')
seven_hearts = pygame.image.load('7_of_hearts.png')

eight_clubs = pygame.image.load('8_of_clubs.png')
eight_spades = pygame.image.load('8_of_spades.png')
eight_diamonds = pygame.image.load('8_of_diamonds.png')
eight_hearts = pygame.image.load('8_of_hearts.png')

nine_clubs = pygame.image.load('9_of_clubs.png')
nine_spades = pygame.image.load('9_of_spades.png')
nine_diamonds = pygame.image.load('9_of_diamonds.png')
nine_hearts = pygame.image.load('9_of_hearts.png')

ten_clubs = pygame.image.load('10_of_clubs.png')
ten_spades = pygame.image.load('10_of_diamonds.png')
ten_diamonds = pygame.image.load('10_of_hearts.png')
ten_hearts = pygame.image.load('10_of_spades.png')

jack_clubs = pygame.image.load('jack_of_clubs.png')
jack_spades = pygame.image.load('jack_of_spades.png')
jack_diamonds = pygame.image.load('jack_of_diamonds.png')
jack_hearts = pygame.image.load('jack_of_hearts.png')

queen_clubs = pygame.image.load('queen_of_clubs.png')
queen_spades = pygame.image.load('queen_of_spades.png')
queen_diamonds = pygame.image.load('queen_of_diamonds.png')
queen_hearts = pygame.image.load('queen_of_hearts.png')

king_clubs = pygame.image.load('king_of_clubs.png')
king_spades = pygame.image.load('king_of_spades.png')
king_diamonds = pygame.image.load('king_of_diamonds.png')
king_hearts = pygame.image.load('king_of_hearts.png')

ace_clubs = pygame.image.load('ace_of_clubs.png')
ace_spades = pygame.image.load('ace_of_spades.png')
ace_diamonds = pygame.image.load('ace_of_diamonds.png')
ace_hearts = pygame.image.load('ace_of_hearts.png')

cardImg.append([ace_clubs, ace_diamonds, ace_hearts, ace_spades])
cardImg.append([two_clubs, two_diamonds, two_hearts, two_spades])
cardImg.append([three_clubs, three_diamonds, three_hearts, three_spades])
cardImg.append([four_clubs, four_diamonds, four_hearts, four_spades])
cardImg.append([five_clubs, five_diamonds, five_hearts, five_spades])
cardImg.append([six_clubs, six_diamonds, six_hearts, six_spades])
cardImg.append([seven_clubs, seven_diamonds, seven_hearts, seven_spades])
cardImg.append([eight_clubs, eight_diamonds, eight_hearts, eight_spades])
cardImg.append([nine_clubs, nine_diamonds, nine_hearts, nine_spades])
cardImg.append([ten_clubs, ten_diamonds, ten_hearts, ten_spades])
cardImg.append([jack_clubs, jack_diamonds, jack_hearts, jack_spades])
cardImg.append([queen_clubs, queen_diamonds, queen_hearts, queen_spades])
cardImg.append([king_clubs, king_diamonds, king_hearts, king_spades])

keys = pygame.key.get_pressed()


def firstStart():
    reset()
    screen.fill((0, 128, 0))
    label = myfont.render('Welcome to Black Jack!', 1, (255, 255, 255))
    label2 = myfont.render('Press space to start', 1, (255, 255, 255))
    screen.blit(label2, (225, 550))
    screen.blit(label, (175, 400))
    pygame.display.update()
    #pygame.init()
    while True:
        clock.tick(60)
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.KEYDOWN:
            dealplayer(675, 650)
            dealplayer(500, 650)
            dealplayer(675, 50)
            dealplayer(500, 50)
            main()


def restart():
    screen.fill((0, 128, 0))
    pygame.display.update()
    pygame.init()

    while True:
        clock.tick(60)
        dealplayer(675, 650)
        dealplayer(500, 650)
        dealplayer(675, 50)
        dealplayer(500, 50)
        main()


def reset():
    global onTable
    global cardImg
    global topCards
    onTable = []
    topCards = []
    time.sleep(1)


def dealplayer(x, y):
    endx = x
    endy = y

    screen.fill((0, 128, 0))
    drawCard(cardBack, endx, endy)
    for a in range(len(onTable)):
        drawCard(onTable[a][0], onTable[a][1], onTable[a][2])
    clock.tick(60)
    drawCard(cardBack, 15, 15)
    pygame.display.update()
    onTable.append([cardBack, x, y])


def dealplayerHit(hit, x, y):
    endx = x
    endy = y

    screen.fill((0, 128, 0))
    drawCard(cardBack, endx, endy)
    for a in range(len(onTable)):
        drawCard(onTable[a][0], onTable[a][1], onTable[a][2])
    clock.tick(60)
    drawCard(cardBack, 15, 15)
    pygame.display.update()
    onTable.append([hit, x, y])


def updateScore(turn=False):
    dScore = d.getScore()
    pScore = p.getScore()
    score1 = smallFont.render(str(dScore), 1, (255, 255, 255))
    score2 = smallFont.render(str(pScore), 1, (255, 255, 255))
    screen.blit(score2, (1150, 600))
    if turn:
        screen.blit(score1, (1150, 50))


def cardImage(n, suit):

    if suit == 'C':
        return cardImg[n][0]
    elif suit == 'D':
        return cardImg[n][1]
    elif suit == 'H':
        return cardImg[n][2]
    elif suit == 'S':
        return cardImg[n][3]


def drawCard(img, x, y):
    white = (255, 255, 255)
    w = 130
    h = 181
    pygame.draw.rect(screen, white, (x - 5, y - 4, w + 10, h + 8), 0)
    newIMG = pygame.transform.scale(img, (w, h))
    screen.blit(newIMG, (x, y))


def main():
    # DRAWING AND INIT
    # VARIABLES
    global d
    global p
    deck = casino.cards()
    cardlist = deck.getCards()
    d = casino.dealer(cardlist)
    p = casino.player(cardlist)
    playerCards = p.deal()
    dealerCards = d.deal()
    allowHit = False
    playerReveal = False
    playerTurn = True
    playerStay = False
    onTable[2] = [cardImage(dealerCards[0][0], dealerCards[0][1]), 675, 50]
    onTable[3] = [cardBack, 500, 50]
    while True:
        pygame.display.update()
        #clock.tick(60)
        # PLAYER DECISION
        if playerReveal == False:
            drawCard(cardBack, 675, 650)
            drawCard(cardBack, 500, 650)
            label = smallFont.render('Press space to reveal cards', 1, (255, 255, 255))
            screen.blit(label, (430, 500))
            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    # Show cards
                    playerReveal = True
                    allowHit = True
                    drawCard(cardImage(playerCards[0][0], playerCards[0][1]), 675, 650)
                    drawCard(cardImage(playerCards[1][0], playerCards[1][1]), 500, 650)
                    onTable[0] = [cardImage(playerCards[0][0], playerCards[0][1]), 675, 650]
                    onTable[1] = [cardImage(playerCards[1][0], playerCards[1][1]), 500, 650]
                    pygame.draw.rect(screen, (0, 128, 0), (429, 849, 550, 100))
            pygame.display.update()
        else:
            label = smallFont.render('Press space to hit and tab to stay', 1, (255, 255, 255))
            screen.blit(label, (350, 550))
            updateScore()
            pygame.display.update()

            ev = pygame.event.poll()
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_TAB:
                    playerStay = True
                    updateScore(True)
                if ev.key == pygame.K_SPACE:

                    if allowHit:
                        hitCard = p.hit()
                        if len(p.PlayerCards) == 3:
                            dealplayerHit(cardImage(hitCard[0], hitCard[1]), 325, 650)
                            drawCard(cardImage(hitCard[0], hitCard[1]), 325, 650)
                            updateScore()
                        elif len(p.PlayerCards) == 4:
                            dealplayerHit(cardImage(hitCard[0], hitCard[1]), 850, 650)
                            drawCard(cardImage(hitCard[0], hitCard[1]), 850, 650)
                            updateScore()
                        elif len(p.PlayerCards) == 5:
                            dealplayerHit(cardImage(hitCard[0], hitCard[1]), 150, 650)
                            drawCard(cardImage(hitCard[0], hitCard[1]), 150, 650)
                            updateScore()
                        elif len(p.PlayerCards) == 6:
                            dealplayerHit(cardImage(hitCard[0], hitCard[1]), 1025, 650)
                            drawCard(cardImage(hitCard[0], hitCard[1]), 1025, 650)
                            updateScore()
                    allowHit = True
                    pygame.display.update()
            if p.getScore() > 21:
                label = myfont.render('You Went Over 21 :( You Lose', 1, (255, 255, 255))
                screen.blit(label, (300, 430))
                allowHit = False
                pygame.display.update()
                time.sleep(1)
                pygame.draw.rect(screen, (0, 128, 0), (0, 640, 1300, 200))
                pygame.draw.rect(screen, (0, 128, 0), (200, 40, 1300, 200))
                pygame.display.update()
                break

            elif p.getScore() == 21 and len(p.PlayerCards) == 2:
                allowHit = False
                label = myfont.render('BLACK JACK!', 1, (255, 255, 255))
                screen.blit(label, (420, 430))
                pygame.display.update()
                time.sleep(1)
                pygame.draw.rect(screen, (0, 128, 0), (0, 640, 1300, 200))
                pygame.draw.rect(screen, (0, 128, 0), (200, 40, 1300, 200))
                pygame.display.update()
                break

            elif playerStay:
                playerTurn = False
                allowHit = False
                updateScore()
                pygame.display.update()

        # dealer
        if playerTurn == False:
            drawCard(cardImage(dealerCards[1][0], dealerCards[1][1]), 500, 50)
            try:
                ind = onTable.index([cardBack, 500, 50])
                onTable[ind] = [cardImage(dealerCards[1][0], dealerCards[1][1]), 500, 50]
            except:
                pass
            updateScore()
            if len(d.dealercards) > 2:
                dealplayerHit(cardImage(dealerCards[2][0], dealerCards[2][1]), 325, 50)
                drawCard(cardImage(dealerCards[2][0], dealerCards[2][1]), 325, 50)
                pygame.display.update()
                time.sleep(0.3)
            if len(d.dealercards) > 3:
                dealplayerHit(cardImage(dealerCards[3][0], dealerCards[3][1]), 850, 50)
                drawCard(cardImage(dealerCards[3][0], dealerCards[3][1]), 850, 50)
                pygame.display.update()
                time.sleep(0.3)
            if len(d.dealercards) > 4:
                dealplayerHit(cardImage(dealerCards[4][0], dealerCards[4][1]), 150, 50)
                drawCard(cardImage(dealerCards[4][0], dealerCards[4][1]), 150, 50)
                pygame.display.update()
                time.sleep(0.3)
            if len(d.dealercards) > 5:
                dealplayerHit(cardImage(dealerCards[5][0], dealerCards[5][1]), 1025, 50)
                drawCard(cardImage(dealerCards[5][0], dealerCards[5][1]), 1025, 50)
                pygame.display.update()
                time.sleep(0.3)
            updateScore(True)

            if d.getScore() > p.getScore():
                if d.getScore() < 22:
                    label = myfont.render('You Lost', 1, (255, 255, 255))
                    screen.blit(label, (510, 430))
                    pygame.display.update()
                    break

                else:
                    label = myfont.render('Dealer Bust\'s, You Win', 1, (255, 255, 255))
                    screen.blit(label, (230, 430))
                    pygame.display.update()
                    break

            elif d.getScore() < p.getScore():
                label = myfont.render('Winner!', 1, (255, 255, 255))
                screen.blit(label, (475, 430))
                pygame.display.update()
                break

            else:
                label = myfont.render('Tie', 1, (255, 255, 255))
                screen.blit(label, (600, 450))
                pygame.display.update()
                break

        else:
            drawCard(cardImage(dealerCards[0][0], dealerCards[0][1]), 675, 50)
            drawCard(cardBack, 500, 50)
    time.sleep(1)

    reset()
    restart()


firstStart()
