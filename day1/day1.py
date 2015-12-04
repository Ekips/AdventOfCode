#!/usr/bin/python
with open ("day1.txt", "r") as f:
    s=f.readlines()
f, t, b = 0, 0, 0
for c in s[0]:
     t+=1
     if c is ')': 
         f-=1
     if c is '(':
         f+=1
     if f < 0 and b == 0:
         b = t
print('Floor: %r' % f)
print('Basement: %r' % b)
