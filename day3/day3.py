#!/usr/bin/python
#2341

with open ("day3.txt", "r") as f:
    s=f.readlines()
w = [[0 for x in range(200)] for x in range(200)]
x, y, i, j, t = 100, 100, 100, 100, 0
r = True
w[x][y]+=1
for c in s[0]:
    if r is True:
        if c is '>': 
            x+=1
        if c is '<':
            x-=1
        if c is '^':
            y+=1
        if c is 'v':
            y-=1
        w[x][y]+=1
        r = False
    elif r is False:
        if c is '>':
            i+=1
        if c is '<':
            i-=1
        if c is '^':
            j+=1
        if c is 'v':
            j-=1
        w[i][j]+=1
        r = True

for x in range(200):
     for y in range(200):
         if w[x][y] > 0:
             t+=1
print('Houses: %r' % t)
