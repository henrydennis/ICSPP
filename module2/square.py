x = int(input("number to square: "))
ans = 0
itersLeft = x
while itersLeft != 0:
    ans += x
    itersLeft -= 1
print(ans)