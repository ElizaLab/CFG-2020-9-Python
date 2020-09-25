import random

random_integer = random.randint(1, 100)

print(random_integer)

user_input = int(input('guess a number'))

if user_input == random_integer:
    print("amazing you got it correct!")
else:
    print('better luck next time :D')


# task 1) change the program so that if I guess above it tells me my guess is too high

# task 2) change the program so that if I guess under it tells me my guess is too low

# task 3) change the program so that iit's inside a while loop and I only get 5 guesses :D