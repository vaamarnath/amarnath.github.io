#!/usr/bin/python
import sys

def checkMultiple(number) :
    digits = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    while number != 0 :
        digit = number % 10
        number = number / 10
        digits[str(digit)] += 1
    
    distinct = 0
    for i in range(0, 10) :
        if digits[str(i)] != 0 :
            distinct += 1

    return distinct


number = int(sys.argv[1])
counter = 1
while True :
    multiple = number * counter
    if checkMultiple(multiple) == 1 :
        print "Found the multiple with least number of distinct digits"
        print multiple, counter
        break

    counter += 1
    print multiple,

