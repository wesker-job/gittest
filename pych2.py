#!/usr/bin/env python3
strEX = "hello world!"
str1 = strEX[0:5]
str2 = strEX[0:10:2]
print(strEX+" - "+str1+" - "+str2)

strArray = ["aa","bb","cc"]
strLink = "**".join(strArray)
print(strLink)
strLink = "--".join(reversed(strArray))
print(strLink)
print(strLink.split("--"))

print("show '{strEX}' and show '{strLink}'".format(**locals()))
print("{0:*^20}".format(strEX))


