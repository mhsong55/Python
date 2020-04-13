from PIL import Image
import pytesseract as pyocr
import wx
import time
import pyautogui as pag
import cv2

pyocr.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def ImagePreTreat(Num):
    image = cv2.imread('./current_price/trade{}.bmp'.format(Num), cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    black_image = cv2.bitwise_not(gray)
    cv2.imwrite('./ImageTest/TreatedImage{}.bmp'.format(Num), black_image)
    print("TreatedImage{}.bmp 파일 생성 완료".format(Num))

def TextExtract(image_addr, text_addr, lang, Count):
    fout = open(text_addr+'/data{}.txt'.format(Count), 'wb')
    readtext = str(pyocr.image_to_string(image_addr+'{}.bmp'.format(Count), lang=lang))
    fout.write(readtext.encode("UTF-8"))
    fout.close()


image_addr = './ImageTest/TreatedImage'
text_addr = './PriceData'

'''
Count = 0
lang = 'eng'
fout = open(text_addr + '/data.txt', 'wb')
readtext = str(pyocr.image_to_string(image_addr + '{}.bmp'.format(Count), lang=lang))
print(readtext)
fout.write(readtext.encode("UTF-8"))
fout.close()
'''

for i in range(138):
    TextExtract(image_addr, text_addr, 'eng', i)
    print('{}번 이미지 작업 완료'.format(i))
'''
Num = 0
ImagePreTreat(Num)
for i in range(137):
    ImagePreTreat(Num)
    Num += 1
    ImagePreTreat(Num)
    if Num == 137:
        print('Complete pre treatment')

'''
'''
print(pyocr.image_to_string(Image.open('./ImageTest/change_Test1.bmp'), lang='eng'))
cv2.imshow("Black image", black_image)
cv2.waitKey(0)
'''