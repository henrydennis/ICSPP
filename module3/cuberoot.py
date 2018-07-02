cube = int(input("Number: "))
epsilon = 0.0001
guess = 0.0
increment = 0.00001
num_guesses = 0
while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print('num guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed to find root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)