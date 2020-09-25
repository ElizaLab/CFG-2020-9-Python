### Logical and comparission operators
# These equate and evaluate expression and result in True or False

# one equal assings
weather = "rainy"

#Two equal equate
print(weather == 'rainy')
print(weather == 'sunny')


is_rainy = weather == 'rainy'

print("today the weather is rainy: " + str(is_rainy) )


### equating numbers
# the numerical is not equal to the string
print("is numerical 10 equal to string 10?")
print(10 == '10')

print("is 10 bigger or greater than 5?")
print(10 >= 5)


### temperature check if freezeing
print("////////////")
#getting user input and print
temperature_now = input("what is the temperature here and NOW?")
print(temperature_now)

#checking type, changing data type to float, checking type again
#print(type(temperature_now))
temperature_now = float(temperature_now)
#print(type(temperature_now))

is_freezing = temperature_now <= 0
print("it's bellow frezzeing: " + str(is_freezing))

money_available = input('Do you have money available to go to cinema?(y/n)')
response_y = money_available == 'y'

