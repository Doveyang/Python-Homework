# -*- coding: UTF-8 -*-
import random
import string
s = []
i = 0
range1 = string.ascii_letters + string.digits
while i < 15:
    c = random.choice(range1)
    if c not in s:
        i += 1
        s.append(c)

print s
