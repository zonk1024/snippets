#!/usr/bin/env python
import string
import random
chars = string.printable[:94]

#for i, c in enumerate(chars):
#    print i, c

print ''.join(random.sample(chars, 32))
