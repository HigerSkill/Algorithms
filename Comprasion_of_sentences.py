import re
import numpy
import scipy.spatial

file = open('text.txt', 'r')

lines = [line.lower() for line in file]
with open('text.txt', 'w') as out:
     out.writelines(sorted(lines))

file = open('text.txt', 'r')

op = []

"""Divide text into words"""
for s in file:
    op.append(re.split('[^a-z]', s))    

v = []
c = 0
"""Delete spaces"""
while c < len(op):
    v.append(filter(None, op[c]))       
    c = c+1

i, n, lcount = 0, 0, 0
unic = {}
while i < len(v):
    for ch in v[i]:
        if ch not in unic:
            unic[ch] = {
                "index": n,
                "occ": [0] * 22
            }
            n += 1
        elif unic[ch]["occ"][lcount] != 0:
            continue
        unic[ch]["occ"][lcount] = v[i].count(ch)
    i += 1
    lcount += 1

arr = numpy.zeros((22, len(unic)))

"""The element (i,j) in the matrix
    is equal to the number of
    occurences of the j-th word 
    in the i-th sentences"""
for ch in unic:
    i, j = 0, unic[ch]["index"]
    for occ in unic[ch]["occ"]:
        arr[i, j] = occ
        i += 1

distantion = []
first_sent = arr[0,]

for i in range(1, 22):
    sent = arr[i, ]
    distantion.append(scipy.spatial.distance.cosine(first_sent, sent))
