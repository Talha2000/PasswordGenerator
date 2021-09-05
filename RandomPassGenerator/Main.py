import os
import sys
import sqlite3 as db
from datetime import datetime
import re
import string
import random
from typing import Final


class RandomGen(object):
    def __init__(self):
        os.system('cls')
        self.length = int(input("Enter the length of password: "))
        self.s = input("Enter the type of password: ").split(",", 3)
        for i in range(len(self.s)):
            self.s[i] = self.s[i].strip()
        self.letters = list(string.ascii_letters)
        self.symbols = list("!@#$%^&*()")
        self.numbers = list(string.digits)
        self.RegPattern = "([a-zA-Z0-9]+[!@#$%^*()])\w+"
        self.keyWordPass()

    # checks what the keywords is or if there are multiple keywords
    def keyWordPass(self):

        self.lst = []
        # for i in range (self.length):
        #     self.lst.append(random.choice(self.letters))
        # for i in range (self.length):
        #     self.lst.append(random.choice(self.symbols))
        # for i in range (self.length):
        #     self.lst.append(random.choice(self.numbers))
        if 'Letters' in self.s and 'Symbols' in self.s and 'Numbers' in self.s:
            for i in range (self.length):
                self.lst.append(random.choice(self.letters))
                self.lst.append(random.choice(self.symbols))
                self.lst.append(random.choice(self.numbers))

        # optimize later
        elif 'Letters' in self.s and 'Symbols' in self.s:
            for i in range (self.length):
                self.lst.append(random.choice(self.letters))
                self.lst.append(random.choice(self.symbols))

        elif 'Letters' in self.s and 'Numbers' in self.s:
            for i in range (self.length):
                self.lst.append(random.choice(self.letters))
                self.lst.append(random.choice(self.numbers))

        if 'Letters' in self.s:
            for i in range (self.length):
                self.lst.append(random.choice(self.letters))
        if 'Symbols' in self.s:
            for i in range (self.length):
                self.lst.append(random.choice(self.symbols))
        if 'Numbers' in self.s:
            for i in range (self.length):
                self.lst.append(random.choice(self.numbers))

        self.returnPassword()

    # Takes the combination and returns it
    def returnPassword(self):
        random.shuffle(self.lst)
        Final_password = ("".join(self.lst))
        # Check = re.search(self.RegPattern, Final_password)
        print(Final_password)
        
RandomGen()
