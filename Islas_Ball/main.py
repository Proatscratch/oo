import pygame, asyncio

pygame.init()
screen = pygame.display.set_mode((800, 600))

bg = pygame.image.load('Background.png')

bbh = pygame.transform.scale_by(pygame.image.load('basketballhoop.png'), 0.5)
BallPos = [80, 430]
fall = 0
Velocity = [0, 0]
Ball = pygame.transform.scale2x(pygame.image.load('BasketBall.png'))
win = 0
font = pygame.font.SysFont('IMPACT', 50)
start = 0

Wins = 0
Tots = 0
async def main():
    global bg
    global bbh
    global BallPos
    global fall
    global Velocity
    global Ball
    global win
    global font
    global start
    global Wins
    global Tots
    while True:
        screen.fill((255, 255, 255))
        oof = font.render('Hello Young Sir! Welcome to Islas Ball!', 0, (0, 0, 0))
        screen.blit(oof, (400 - oof.get_width() / 2, 10))
        oof = font.render('Islas Ball!', 0, (255, 0, 0))
        screen.blit(oof, (400 - oof.get_width() / 2, 50))

        oof = font.render('Press [Enter] or [Return] to Play Sir!', 0, (0, 0, 0))
        screen.blit(oof, (400 - oof.get_width() / 2, 100))

        oof = font.render('Produced by Sphinx Studios!', 0, (0, 0, 0))
        screen.blit(oof, (400 - oof.get_width() / 2, 150))

        oof = font.render('And MGames!', 0, (0, 0, 0))
        screen.blit(oof, (400 - oof.get_width() / 2, 200))

        oof = font.render('Write it down, Write it all down!', 0, (0, 0, 255))
        screen.blit(oof, (400 - oof.get_width() / 2, 250))

        oof = font.render('Press [Enter] or [Return]', 0, (0, 0, 0))
        screen.blit(oof, (400 - oof.get_width() / 2, 500))

        if pygame.key.get_pressed()[pygame.K_RETURN]:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        pygame.display.update()

    while True:
        screen.blit(bg, (0, 0))
        screen.blit(bbh, (300, 300))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        screen.blit(
            pygame.transform.smoothscale_by(pygame.image.load('Mr Islas.png'),
                                            0.5), (40, 340))
        screen.blit(
            pygame.transform.rotate(Ball,
                                    sum(Velocity) * 10 if fall == 1 else 0),
            BallPos)
        #print(fall)
        if pygame.mouse.get_pressed()[0] and fall == 0:
            fall = 2
            start = 1
        if fall == 2 and not pygame.mouse.get_pressed()[0]:
            fall = 1
        elif fall == 2:
            pygame.draw.line(screen, (200, 200, 200),
                            (BallPos[0] + 20, BallPos[1] + 20),
                            (pygame.mouse.get_pos()), 3)
            Velocity = [(BallPos[0] + 20 - pygame.mouse.get_pos()[0]) / 6,
                        (BallPos[1] + 20 - pygame.mouse.get_pos()[1]) / 4]
            for v in Velocity:
                v /= 10
        if fall == 1:
            Velocity[1] += 1.5
            BallPos[0] += Velocity[0]
            BallPos[1] += Velocity[1]
        if fall == 2:
            win = 0
        #pygame.draw.rect(screen, (0, 0, 0), (404, 300, 32, 70), 2)
        if Velocity[1] > 5 and BallPos[1] < 330 and BallPos[1] > 300 and int(
                BallPos[0]) in range(340, 404):
            win = 1
            Velocity[0] = -2
        if fall == 0 and start:
            if win == 0:
                oof = font.render(
                    f'You lose... Sir, Please write it down next time {round(Wins/Tots*100)}%',
                    0, (125, 0, 255))
                oof2 = font.render(
                    f'You lose... Sir, Please write it down next time {round(Wins/Tots*100)}%',
                    0, (0, 0, 0))
                oof = pygame.transform.scale_by(oof, 0.7)
                oof2 = pygame.transform.scale_by(oof2, 0.7)
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        screen.blit(
                            oof2, (400 - oof.get_width() / 2 + x * 2, 10 + y * 2))
                screen.blit(oof, (400 - oof.get_width() / 2, 10))
            if win:
                oof = font.render(
                    f'You win!! Nice job young sir! {round(Wins/Tots*100)}%', 0,
                    (255, 200, 0))
                oof2 = font.render(
                    f'You win!! Nice job young sir! {round(Wins/Tots*100)}%', 0,
                    (0, 0, 0))
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        screen.blit(
                            oof2, (400 - oof.get_width() / 2 + x * 2, 10 + y * 2))
                screen.blit(oof, (400 - oof.get_width() / 2, 10))

        if abs(Velocity[0]) < 1:
            if BallPos != [80, 430]:
                if win:
                    Wins += 1
                Tots += 1
            BallPos = [80, 430]
            
            fall = 0

        if abs(BallPos[0] - 400) > 400:
            Velocity[0] = 0
        if BallPos[1] > 500 or (int(BallPos[0]) in range(404, 436)
                                and BallPos[1] in range(300, 370)):
            Velocity[1] *= -0.5
            if BallPos[1] > 500:
                BallPos[1] = 500
            else:
                BallPos[1] = 299
                Velocity[0] *= -0.7
                win = 1
            Velocity[0] *= 0.7
        Velocity[0] *= 0.99
        #print(Tots)
        pygame.display.update()
        pygame.time.Clock().tick(30)
        await asyncio.sleep(0)

asyncio .run(main())