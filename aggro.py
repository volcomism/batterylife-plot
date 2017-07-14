#!/usr/bin/env python

import math
from itertools import groupby

def prime_factors(n):
  """ Return the prime factors of the given number. """
  # < 1 is a special case
  if n <= 1:
     return [1]
  factors = []
  lastresult = n
  while True:
     if lastresult == 1:
        break
     c = 2
     while True:
        if lastresult % c == 0:
           break
        c += 1
     factors.append(c)
     lastresult /= c
  return factors

def f(n):
  numstr = ""
  a = prime_factors(n)
  if len(a) == 1:
     print "prime"
     return a[0]
  for key, group in groupby(a):
     p = key
     n = len(list(group))
     numstr += str(p)
     if n > 1:
        numstr += str(n)
  return int(numstr)

if __name__ == '__main__':
  n = 13532385396179
  lastn = 1
  print n
  while n != lastn:
     lastn = n
     n = f(lastn)
     print n
