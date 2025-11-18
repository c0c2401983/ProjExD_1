import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x+1600,0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(kk_img, kk_rct)

        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            up = -1
        else:
            up = 0
        if key_lst[pg.K_DOWN]:
            
            down = 1
        else:
            down = 0

        if key_lst[pg.K_LEFT]:
            left = -1
        else:
            left = 0
        if key_lst[pg.K_RIGHT]:
            right = 1
        else:
            right = -1

        kk_rct.move_ip((right + left ,up + down))

        pg.display.update()
        tmr+=1
        

        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()