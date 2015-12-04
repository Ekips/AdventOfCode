#!/usr/bin/python
with open ("day2.txt", "r") as f:
    s=f.readlines()
t, r = 0, 0
for c in s:
      l = c.rstrip().split('x')
      l, w , h = map(int, l)
      t += 2*((l*w)+(w*h)+(h*l)) + min([l*w, w*h, h*l])
      r += (l*w*h) + 2*min([l+w, w+h, h+l]) 
print('Total: %r' % t)
print('Ribbon: %r' %r)
