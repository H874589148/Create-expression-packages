#-*- coding:utf-8 -*-

import sys
from email.header import UTF8
import importlib
importlib.reload(sys)
#reload(sys)
#sys.setdefaultencoding("gbk")
sys.setdefaultencoding('gbk')

import os
import pygame
from pygame.locals import *

pygame.init()

from PIL import Image, ImageDraw, ImageFont
img = Image.open("head.jpg")  #250*250
jgz = Image.open("face.jpg")  #101*113
img.paste(jgz, (73, 47))  #左右，上下
#img.show()
draw = ImageDraw.Draw(img)
ttfront = ImageFont.truetype('simhei.ttf', 24)
draw.text((32, 190), "你好生的傲娇啊\n   我惹不起".decode('utf8'),fill=(0, 0, 0),font=ttfront)
#img.show()
img.save("_biaoq.jpg")
print('表情包合成完成，请在上查看')