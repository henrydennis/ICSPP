s = 'azcbobobegghakl'

currentsubstring = ""
longestsubstring = ""
currentpos = 0

for pos in range(len(s)):
    currentpos = pos
    currentsubstring = s[currentpos]
    while currentpos + 1 < len(s) and s[currentpos] <= s[currentpos+1]:
        currentsubstring += s[currentpos+1]
        currentpos += 1
    if len(currentsubstring) > len(longestsubstring):
        longestsubstring = currentsubstring
print("Longest substring in alphabetical order is: " + longestsubstring)