import wx
import time
import pyautogui as pag

def capture(position, Num):
    count = 1
    start = time.time()
    app = wx.App()
    screen = wx.ScreenDC()
    for i in range(count):
        bmp = wx.Bitmap(position[2] - position[0], position[3] - position[1])
        mem = wx.MemoryDC(bmp)
        mem.Blit(0, 0, position[2] - position[0], position[3] - position[1],
                 screen, position[0], position[1])
        del mem
        bmp.SaveFile("./current_price/trade{}.bmp".format(Num), wx.BITMAP_TYPE_BMP)
        print("trade{}.bmp 파일 생성 완료".format(Num))


Num = 0
position = [603, 333, 884, 823]
NextButton = [1713, 527]
capture(position, Num)
for i in range(137):
    pag.moveTo(NextButton)
    time.sleep(0.5)
    pag.click()
    time.sleep(0.5)
    Num += 1
    capture(position, Num)
    if Num == 137:
        print('전체 캡쳐 작업 완료되었습니다.')