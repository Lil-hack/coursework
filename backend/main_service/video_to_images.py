import numpy as np
import cv2
import imagehash
from PIL import Image
import time
import json
import sys
import io

start_time = time.time()
video_name='Сериал След «Зайка рыбка птичка…».mp4'
cap = cv2.VideoCapture(video_name)   # /dev/video0

print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
mas_hash=[]
while True:
  ret, frame = cap.read()

  if not ret:
    break
  img = Image.fromarray(frame)
  hash = imagehash.phash(img,8)
  mas_hash.append(str(hash))


with io.open('playlist6.json', 'w') as json_file:
    data = json.dumps(mas_hash)
    json_file.write(data)

print(str(mas_hash))
print (len(mas_hash))
# cv2.imshow('window_name', frame) # show frame on window
# hash = imagehash.average_hash(frame)
hash2 = imagehash.phash(Image.open('Test_gray.jpg'),32)

print(Image.open('Test_gray.jpg'))
# print(hash)
print(hash2)


print("--- %s seconds ---" % (time.time() - start_time))
