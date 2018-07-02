s = 'azcbobobegghakl'

i = 0

vowels = ['a','e','i','o','u']

for letter in s:
    if letter in vowels:
        i += 1
print("Number of vowels:",i)