import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},;:.- /\\?+*# "

upper, lower, nums, syms = True, True, True, True # Can set as false and the compiler will not include the specific characters in the password
all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

length = 8 # the length of characters in the password
amount = 1 # the number of passwords one can generate

for x in range(amount):
    passwrd = "".join(random.sample(all, length))
    print(passwrd)
    