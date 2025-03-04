# handmade LCD font for pygame
# 5x7ドットマトリクス

import param_MCJE as param

# font.txt からフォントデータを読み込む
with open("fonts/font.txt", encoding="utf-8") as f:
    LCD_font_styles = f.read().split("\n")


class LCD_font:
    def __init__(self, mc):
        self.mc = mc

    def init_col(self, COLOR_ON=param.SEA_LANTERN_BLOCK, COLOR_OFF=param.AIR):
        # ひと桁、コラムの設定
        # ブロックのサイズと配置間隔をピクセル指定（インターバル）
        # on/offのカラー
        self.COLOR_ON = COLOR_ON
        self.COLOR_OFF = COLOR_OFF

    def init_row(self, X_ORG=2, Y_ORG=8, Z_ORG=5, COL_INTV=6):  # 表示行の設定
        # xy空間での7セグ表示、最上位桁の左下座標をブロック数で指定
        self.X_ORG = X_ORG
        self.Y_ORG = Y_ORG
        self.Z_ORG = Z_ORG
        # 各桁のブロック間隔をブロック数で指定（インターバル）
        self.COL_INTV = COL_INTV

    def update_col(self, col=0, code=2):  # ある桁にある文字を表示する関数
        # codeの文字をcol桁目に表示、桁は最上位桁の左から右へ進む。
        code = int(code) * 7
        for y in range(7):
            for x in range(5):
                if int(LCD_font_styles[code + y][x]) == 1:
                    color = self.COLOR_ON
                else:
                    color = self.COLOR_OFF
                # 桁の原点
                x0 = self.X_ORG + self.COL_INTV * col
                y0 = self.Y_ORG
                z0 = self.Z_ORG

                # ドットを描く
                # pygame.draw.rect(self.screen, color, Rect(org1[0], org1[1], block_size, block_size))
                self.mc.setBlock(x0 + x, y0 - y, z0, color)
