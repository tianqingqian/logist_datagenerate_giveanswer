# -*- coding:utf-8 -*-
import numpy as np
import random
from PIL import Image,ImageFont,ImageFilter,ImageDraw
import os

def Mkdir(file_path):
    #create package
    if not os.path.isdir(file_path):
        print(file_path+' is not exists')
        os.makedirs(file_path)
        print('Create Success')
    else:
        print(file_path+' is exists')

def CreateFile(newfile):
    #create file
    if not os.path.exists(newfile):
        f = open(newfile, 'w')
        f.close()
        print(newfile + " created.")
    else:
        print(newfile + " already exist.")

# font_path = '/usr/share/fonts/type1/gsfonts/a010015l.pfb'
font_path = '/Library/Fonts/Arial.ttf'
def gene_add():
    CreateFile('./add.txt')
    f1 = open('./add.txt', 'a')
    n = 87
    num = 0
    for i in range(n):
        for j in range(n):
            k = i + j
            a = str(i)
            b = str(j)
            c = str(k)
            result1 = a + '+' + b
            result2 = a + '&' + b
            result = c
            # print result
            f1.write(a + "," + b + "," + c)
            f1.write("\n")
            num1 = str(num)
            im_name1 = './positive_general/' + num1 + '.jpg'
            im_name2 = './positive_special/' + num1 + '.jpg'
            im_name3 = './positive_answer/' + num1 + '.jpg'
            num = num + 1
            saveimg(result1, im_name1)
            # saveimg(result2, im_name2)
            saveimg(result, im_name3)
    f1.close()
def gene_add_f():
    CreateFile('./add_f.txt')
    f1 = open('./add_f.txt', 'a')
    n = 87
    num = 0
    for i in range(n):
        for j in range(n):
            k = i + j
            a = str(i)
            b = str(j)
            c = str(k + random.randint(1,10))
            result1 = a + '+' + b
            result2 = a + '&' + b
            result = c
            # print result
            f1.write(a + "," + b + "," + c)
            f1.write("\n")
            num1 = str(num)
            im_name1 = './negative_general/' + num1 + '.jpg'
            im_name2 = './negative_special/' + num1 + '.jpg'
            im_name3 = './negative_answer/' + num1 + '.jpg'
            num = num + 1
            # saveimg(result1, im_name1)
            # saveimg(result2, im_name2)
            # saveimg(result, im_name3)
    f1.close()
def gene_sub():
    CreateFile('./sub.txt')
    f1 = open('./sub.txt', 'a')
    n = 87
    num = 7500
    for i in range(n):
        for j in range(n):
            k = i + j
            a = str(i)
            b = str(j)
            c = str(k)
            result1 = c + '-' + a
            result2 = c + '^' + a
            result = b
            # print result
            f1.write(c + "," + a + "," + b)
            f1.write("\n")
            num1 = str(num)
            im_name1 = './positive_general/' + num1 + '.jpg'
            im_name2 = './positive_special/' + num1 + '.jpg'
            im_name3 = './positive_answer/' + num1 + '.jpg'
            num = num + 1
            saveimg(result1, im_name1)
            # saveimg(result2, im_name2)
            saveimg(result, im_name3)
    f1.close()
def gene_sub_f():
    CreateFile('./sub_f.txt')
    f1 = open('./sub_f.txt', 'a')
    n = 87
    num = 7500
    for i in range(n):
        for j in range(n):
            k = i + j
            a = str(i)
            b = str(j + random.randint(1, 10))
            c = str(k)
            result1 = c + '-' + a
            result2 = c + '^' + a
            result = b
            # print result
            f1.write(c + "," + a + "," + b)
            f1.write("\n")
            num1 = str(num)
            im_name1 = './negative_general/' + num1 + '.jpg'
            im_name2 = './negative_special/' + num1 + '.jpg'
            im_name3 = './negative_answer/' + num1 + '.jpg'
            num = num + 1
            # saveimg(result1, im_name1)
            # saveimg(result2, im_name2)
            # saveimg(result, im_name3)
    f1.close()
def gene_mul():
    CreateFile('./mul.txt')
    f1 = open('./mul.txt', 'a')
    n = 88
    num = 15000
    for i in range(1,n):
        for j in range(1,n):
            k = i * j
            a = str(i)
            b = str(j)
            c = str(k)
            result1 = a + 'x' + b
            result2 = a + '(' + b
            result = c
            # print result
            f1.write(a + "," + b + "," + c)
            f1.write("\n")
            num1 = str(num)
            im_name1 = './positive_general/' + num1 + '.jpg'
            im_name2 = './positive_special/' + num1 + '.jpg'
            im_name3 = './positive_answer/' + num1 + '.jpg'
            num = num + 1
            saveimg(result1, im_name1)
            # saveimg(result2, im_name2)
            saveimg(result, im_name3)
    f1.close()
def gene_mul_f():
    CreateFile('./mul_f.txt')
    f1 = open('./mul_f.txt', 'a')
    n = 88
    num = 15000
    for i in range(1,n):
        for j in range(1,n):
            k = i * j
            a = str(i)
            b = str(j)
            c = str(k + random.randint(1, 10))
            result1 = a + 'x' + b
            result2 = a + '(' + b
            result = c
            # print result
            f1.write(a + "," + b + "," + c)
            f1.write("\n")
            num1 = str(num)
            im_name1 = './negative_general/' + num1 + '.jpg'
            im_name2 = './negative_special/' + num1 + '.jpg'
            im_name3 = './negative_answer/' + num1 + '.jpg'
            num = num + 1
            # saveimg(result1, im_name1)
            # saveimg(result2, im_name2)
            # saveimg(result, im_name3)
    f1.close()
def gene_div():
    CreateFile('./div.txt')
    f1 = open('./div.txt', 'a')
    n = 88
    num = 22500
    for i in range(1,n):
        for j in range(1,n):
            k = i * j
            a = str(i)
            b = str(j)
            c = str(k)
            result1 = c + '/' + a
            result2 = c + 'T' + a
            result = b
            # print result
            f1.write(c + "," + a + "," + b)
            f1.write("\n")
            num1 = str(num)
            im_name1 = './positive_general/' + num1 + '.jpg'
            im_name2 = './positive_special/' + num1 + '.jpg'
            im_name3 = './positive_answer/' + num1 + '.jpg'
            num = num + 1
            saveimg(result1, im_name1)
            saveimg(result2, im_name2)
            saveimg(result, im_name3)
    f1.close()

def gene_div_f():
    CreateFile('./div_f.txt')
    f1 = open('./div_f.txt', 'a')
    n = 88
    num = 22500
    for i in range(1,n):
        for j in range(1,n):
            k = i * j
            a = str(i)
            b = str(j + random.randint(1, 10))
            c = str(k)
            result1 = c + '/' + a
            result2 = c + 'T' + a
            result = b
            # print result
            f1.write(c + "," + a + "," + b)
            f1.write("\n")
            num1 = str(num)
            im_name1 = './negative_general/' + num1 + '.jpg'
            im_name2 = './negative_special/' + num1 + '.jpg'
            im_name3 = './negative_answer/' + num1 + '.jpg'
            num = num + 1
            # saveimg(result1, im_name1)
            # saveimg(result2, im_name2)
            # saveimg(result, im_name3)
    f1.close()
def saveimg(text,im_name):
    font = ImageFont.truetype(font=font_path, size=16)
    im = Image.new("1", (60, 16), 1)
    dr = ImageDraw.Draw(im)
    sz = font.getsize(text)
    dr.text((60 - sz[0], -1), text, fill='#000000', font=font)
    # dr.text((0, -1), text, fill='#000000', font=font)
    im.save(im_name)

if __name__ == '__main__':
    gene_add()
    gene_sub()
    gene_mul()
    gene_div()
    print()