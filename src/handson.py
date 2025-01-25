import pygame as pg

# 画面の幅と高さ
W, H = 320, 270

TILE_X = 16
TILE_Y = 14

def main():
    # pygameの初期化
    pg.init()
    # 画面の初期化
    win = pg.display.set_mode((W, H))
    pg.display.set_caption("Hello Pygame")
    # クロックの初期化
    # クロックはフレームレートを制御するために使用される(1秒間に何コマ動くか？)
    clock = pg.time.Clock()

    # ゲームループ
    while True:
        # イベントの処理(FIFOでイベントが溜まる)
        # イベントとは、キーボードやマウスの入力、ウィンドウのリサイズ、ウィンドウの閉じるボタンのクリックなどのこと
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    pg.quit()
        # 画面の塗りつぶし
        win.fill((135, 206, 235))
        # 画面の更新
        pg.display.flip()
        
        # フレームレートの設定
        clock.tick(30)

if __name__ == "__main__":
    main()