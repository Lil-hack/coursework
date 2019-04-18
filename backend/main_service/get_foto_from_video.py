import numpy as np
import cv2
import imagehash
from PIL import Image
import time
import json
import sys
import io

video_name='Whatsapp Love Status Video2017(20Sec).mp4'
cap = cv2.VideoCapture(video_name)
cap.set(cv2.CAP_PROP_POS_FRAMES, 200-1)
res, frame = cap.read()
cv2.imwrite('l.jpeg',frame)
cv2.imwrite('l.jpg',frame)
cv2.imwrite('l.png',frame)

i = Image.open('lox.jpeg')
i2 = Image.open('lox.jpg')
i3 = Image.open('lox.png')
i4 = Image.open('lox2.png')
i5 = Image.open('test.png')

j = Image.open('l.jpeg')
j2 = Image.open('l.jpg')
j3 = Image.open('l.png')


hash = imagehash.phash(i,32,2)
hash2 = imagehash.phash(i2,32,2)
hash3 = imagehash.phash(i3,32,2)
hash4 = imagehash.phash(i4,32,2)
hash5 = imagehash.phash(i5,32,2)

hashj = imagehash.phash(j,32,2)
hashj2 = imagehash.phash(j2,32,2)
hashj3 = imagehash.phash(j3,32,2)

print(hash)
print(hash2)
print(hash3)
print(hash4)
print(hash5)


print()
print(hashj)
print(hashj2)
print(hashj3)

print(hash-hash2)
print(hash-hash3)
print(hash-hash4)
print(hash-hash5)

print()

print(hash-hashj2)
print(hash-hashj3)
print(hash-hashj)