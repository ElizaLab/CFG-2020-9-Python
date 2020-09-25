# Control flow
#if statements

# syntax
# if <condition>: #checks this first
    # block of code
# elif <condition>: #checks if the above WAS NOT true.
    # block of code
# else: # runs this code if everything else was false
    # block of code

counter = 0

while counter < 10:
    print("counter at :" + str(counter))
    password = input('password: ')
    if password == 'jumanji':
        print('Success!')
        print("logged in as a normal user")
    elif password == 'admin':
        print('Success!')
        print('logged in as admin!')
    else:
        print('try again')

    counter = counter + 1


print(">>>end program")

