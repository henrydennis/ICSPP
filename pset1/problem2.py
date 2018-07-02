s = 'azcbobobegghakl'

i = 0

for letter in range(len(s)-2):
    if s[letter:letter+3] == 'bob':
        i += 1
print("Number of vowels:",i)