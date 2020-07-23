#! /usr/bin/env python3
# Tried to make some encodings like the SHA-1 encryption or "just like that" stuff
import random, os
os.system("clear")

# 1
lower_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# 2
upper_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers are at [0]
symbols = list("@#$%") # -1
used_char = set()
while len(used_char) < 40:
    number, lower_alph = str(random.randint(0, 9)), lower_alpha[random.randint(0, 25)]
    upper_alph, symbol = upper_alpha[random.randint(0, 25)], symbols[random.randint(0, 3)]
    used_char.add(number); used_char.add(lower_alph); used_char.add(upper_alph); used_char.add(symbol)

if len(used_char) > 40:
    while len(used_char) != 40:
        used_char.pop()
print("".join(used_char), len(used_char))