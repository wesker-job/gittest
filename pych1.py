#!/usr/bin/env python

def doubleV(dValue):
  return dValue*2

print("Hello", "World!")

a = 5
if a > 10:
  print ("a > 10")
elif a > 0:
  print ("a > 0")
else:
  print ("a < 0")

b = 0
while b<2:
  b = b + 1
  print("b"+str(b))

strSh = ""
for sh in ["a","b","c"]:
  strSh += sh + ","
print(strSh)

try:
  line = int(input("input int value:"))
  DoubV = doubleV(line)
  print ("def value("+str(line)+"):"+str(DoubV))
except ValueError as err:
  print(err)

import random
x = random.randint(1,6)
y = random.choice(["apple","banana","cherry"])
print(str(x)+", "+y)
