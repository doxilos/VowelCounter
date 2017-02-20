import sys
import os


class VowelCounter:
    def count(uin):
        letters = list(uin)
        vowels = ["a","e","ı","o"]
        count = 0
        for i in range(0,len(letters)):
            if letters[i] in vowels:
                count += 1
        print(count)
    count(input("String"))
