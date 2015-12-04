#!/usr/bin/python
import hashlib
v = 'bgvyzdsv'
c = 0
while 1:
    c+=1
    r = hashlib.md5(v + str(c)).hexdigest()
    if r.find('000000') == 0:
        print('md5: %r' % r)
        print('number: %r' % c)
        break 
