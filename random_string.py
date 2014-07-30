#!/usr/bin/env python
import string
import random
chars = string.printable[:94]

#for i, c in enumerate(chars):
#    print i, c

print ''.join(chars[random.randint(0, len(chars) - 1)] for i in range(32))
