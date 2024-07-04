import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:.- /\\?+*# "

upper, lower, nums, syms = True, True, True, True
all = ""

if upper:
    all += uppercase_letters
else:
    all += lowercase_letters
if nums:
    all += nums
else:
    all += syms

length = 20 # the length of characters in the password
amount = 10 # the number of passwords one can generate

for x in range(amount):
    passwrd = "".join(random.sample(all, length))
    print(passwrd)
    