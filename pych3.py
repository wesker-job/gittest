#!/usr/bin/env python3
t = "aa","bb","cc",25
print("bb:"+str(t.count("bb"))+", "+t[1])
print(str(t[1:])+", "+str(t[0:1]))

L = [1,2,3]
print(L)
L.append(4)
print(L)
L.insert(1,5)
print(L)
L.sort()
print(L)
L.reverse()
print(L)
print(L[1:3])

leaps = [y for y in range(1900, 1940)
         if (y % 4 == 0 and y % 100 !=0) or (y % 400 == 0)]
print(leaps)

codes = [s + z + c for s in "MF" for z in "SMLX" for c in "BGW"
         if not (s == "F" and z == "X")]
print(codes)
