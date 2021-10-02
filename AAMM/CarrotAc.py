from time import time, sleep
from tkinter import *
from typing import Text
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import os
from PIL import Image
import pyautogui
import eel
import pyowm
import pytesseract
from threading import *


eel.init("web")


eel.start("design.html", size = (340, 550))
# pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


# def serchWord():
#     while True:
#         picture = 'image.png'
#         screen = np.array(ImageGrab.grab(bbox=(599, 261, 1316, 565)))
#         # print('loop took {} seconds'.format(time.time()-last_time))
#         # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
#         cv2.imwrite(picture, screen)
#         img = cv2.imread('image.png')
#         text = pytesseract.image_to_string(img)
#         serch = text.find("ACCEPT")
#         if serch == -1:
#             print("serch")
#         else:
#             pyautogui.moveTo(942, 429)
#             pyautogui.click()
#             break







# # // Design //
# #Window
# root = Tk()
# root.resizable( width = False, height = False)
# root.geometry("300x320")
# root.title("Accepter")
# root["bg"] = "#242424"
# root.iconbitmap( "D:\PM\AAMM\Aacceptimage.ico" )
# #Event
# start_script = Button(text = "start", font = "18", bg = "#e3e3e3", fg = "#0f0f0f",relief = "solid", activebackground = "silver", width = "10", height = "3", activeforeground = "#0f0f0f", command = serchWord)
# stop_script = Button(text = "stop", font = "18", bg = "#e3e3e3", fg = "#0f0f0f",relief = "solid", activebackground = "silver", width = "10", height = "1", activeforeground = "#0f0f0f")
# text_login = Label(text = "Enter acept word", font = "18", fg = "#e3e3e3", bg = "#242424")
# login = Entry( root, font = "18", fg = "#e3e3e3", relief = "solid" , justify = "left")


# text_login.pack()
# login.pack()
# text_login.place( x = 90, y = 115)
# login.place( x = 60, y = 147)
# start_script.place( x = 100, y = 200)
# stop_script.place( x = 100, y = 250)
# root.mainloop()