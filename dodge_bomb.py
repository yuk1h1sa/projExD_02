import random
import sys

import pygame as pg


delt = {pg.K_UP: (0,-1),
        pg.K_DOWN: (0,+1),
        pg.K_LEFT: (-1,0),
        pg.K_RIGHT: (+1,0)
        }

kk_img = pg.image.load("ex02/fig/3.png")

kk_img_a = {(+1,0):pg.transform.rotozoom(kk_img, 0, 2.0),        #こうかとんの向きとそれに対応する画像のリスト
            (+1,-1):pg.transform.rotozoom(kk_img, 45, 2.0),
            (0,-1):pg.transform.rotozoom(kk_img, 90, 2.0),
            (-1,-1):pg.transform.rotozoom(kk_img, 135, 2.0),
            (-1,0):pg.transform.rotozoom(kk_img, 180, 2.0),
            (-1,+1):pg.transform.rotozoom(kk_img, 225, 2.0),
            (0,+1):pg.transform.rotozoom(kk_img, 270, 2.0),
            (+1,+1):pg.transform.rotozoom(kk_img, 315, 2.0)
            }

def check_bound(scr_rct: pg.Rect,obj_rct:pg.Rect):
    """
    オブジェクトが画面内か画面外かを判定する関数
    引数1:画面SurfaceのRect
    引数2:こうかとん、または爆弾SurfaceのRect
    戻り値:横方向、縦方向のはみ出し判定結果（画面内:Ture/画面外:False）
    """
    yoko,tate = True,True
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = False
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = False
    return yoko, tate


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))

    clock = pg.time.Clock()
    
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")

    kk_img = pg.image.load("ex02/fig/3.png")

    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)

    kk_img_1 =pg.image.load("ex02/fig/6.png")

    kk_img_2 = pg.transform.rotozoom(kk_img_1,0,2.0)

    tmr = 0

    bb_img = pg.Surface((20,20))

    pg.draw.circle(bb_img,(255,0,0),(10,10),10)

    bb_img.set_colorkey((0,0,0))

    bb_x = random.randint(0,1600)  #爆弾のx座標
    bb_y = random.randint(0,900)  #爆弾のy座標

    vx,vy = +1,+1

    bb_rct = bb_img.get_rect()
    bb_rct.center = bb_y,bb_x

    kk_rct = kk_img.get_rect()
    kk_rct.center = 900,400

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return 0

        tmr += 1

        key_lst = pg.key.get_pressed()

        for k,mv in delt.items():

            if key_lst[k]:

                kk_rct.move_ip(mv)

        if check_bound(screen.get_rect(), kk_rct) != (True, True):

            for k, mv in delt.items():

                if key_lst[k]:

                    kk_rct.move_ip(-mv[0], -mv[1]) 

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct)
        bb_rct.move_ip(vx,vy)

        yoko, tate = check_bound(screen.get_rect(), bb_rct)
        if not yoko:
            vx *= -1
        if not tate:
            vy *= -1
        
        screen.blit(bb_img,bb_rct)
        
        if kk_rct.colliderect(bb_rct):
            clock.tick(0.1)
            screen.blit(kk_img_2,[800,450])
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()