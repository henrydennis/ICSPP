cube = int(input("number: "))
for guess in range(cube+1):
    if guess**3 == cube:
        print("Cube root of", cube, "is", guess)
        break
    if guess**3 > cube:
        print("No perfect cube root for", cube)
        break