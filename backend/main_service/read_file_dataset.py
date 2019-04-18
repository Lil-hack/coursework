import numpy as np
import cv2
import imagehash
from PIL import Image
import time
import json
import sys
import io
import threading
import pybktree


def fuzzy_distance(s1, s2):
    # similarity = fuzz.token_sort_ratio(s1, s2)
    # distance = -1 * (similarity - 100)
    distance=imagehash.hex_to_hash(s1)-imagehash.hex_to_hash(s2)
    return distance


def worker(start,end,data,hash):

    print('start '+str(start))
    print('end  '+str(end))
    for i in range(start, end):
        imagehash.hex_to_hash(data[i])-hash

    print("--- %s seconds ---" % (time.time() - start_time))
    return


start_time = time.time()
data = []
with open('playlist6.json', 'r') as f:
    data = json.loads(f.read())

last_foto='f2f3cccc33262a23'
hash=imagehash.hex_to_hash(last_foto)
print(hash)
np_data=np.asarray(data)
print(np_data)
print(len(np.unique(np_data))//5)
# count_threads=2
# part_data=len(data)//count_threads
# threads = []
# for i in range(1,count_threads+1):
#     print(i*part_data)
#     if i*part_data-part_data<0:
#         start=0
#     else:
#         start=i*part_data-part_data
#
#     end=i*part_data
#     t = threading.Thread(target=worker, args=(start,end,data,hash))
#     threads.append(t)
#     t.start()
# print(list(data))
tree = pybktree.BKTree(fuzzy_distance, np_data)

print(tree.find(last_foto, 10))

print(tree)


# for foto in data:
    # tree.add(convert_base(last_foto,from_base=16,to_base=16))
   # print(foto)
   # print(hash)
   # print(imagehash.hex_to_hash(foto)-hash)
   # hash=imagehash.hex_to_hash(foto)



print("--- %s seconds main ---" % (time.time() - start_time))

name = "not_aneta"

while name!= "aneta":

    name = input()
    start_time2 = time.time()
    print(tree.find(name, 10))
    print("--- %s seconds main ---" % (time.time() - start_time2))