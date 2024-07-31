import pyautogui as pg
import time

pg.press('win')
time.sleep(5)
pg.write('google chrome')
time.sleep(5)
pg.press('enter')
time.sleep(5)
pg.write('Youtube')
time.sleep(2)
pg.press('enter')
time.sleep(5)
pg.click(x=1384, y=147)
time.sleep(5)
pg.click(x=1158, y=206)


"""
QUANDO FOREM USAR ESSE CODIGO SE ATENTEM EM MUDAR A LOCALIZAÇÃO DO MOUSE, POIS DEPENDENDO DO
TAMANHO DO SEU MUNITOR AS CORDENADAS MUDAM.

ESPERO QUE APROVEITEM E USEM A CREATIVIDADE PARA FAZER OUTRAS AUTOMAÇOS.

"""