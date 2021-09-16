# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def longestword(filename):
        with open(filename, 'r+') as f:
                words = f.read().split()
                max_len_word = max(words,key=len)
                max_len = len(max(words,key=len))
                print('maximum lenth word in file :',max_len_word)
                print('lenth is :',max_len)


import functools