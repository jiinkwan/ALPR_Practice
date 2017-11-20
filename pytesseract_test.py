"""
Project Name: ALPR_Practice

File Name: pytesseract_test 

Created by: HongJi

Date: 2017-11-14 14 오후 1:34 


"""

import sys
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter, ImageOps

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

im = Image.open("C:/Users/Hongji/Documents/GitHub/\ALPR_Practice/Bullitt_Movie_plate.jpg") # the second one
im.load()
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('C:/Users/Hongji/Documents/GitHub/\ALPR_Practice/Bullitt_Movie_plate_2.jpg')
text = pytesseract.image_to_string(Image.open('C:/Users/Hongji/Documents/GitHub/\ALPR_Practice/Bullitt_Movie_plate_2.jpg'))
print(text)