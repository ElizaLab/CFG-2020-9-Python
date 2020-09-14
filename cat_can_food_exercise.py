#Exercise 1.4: In a new Python file called cat_food.py, create a program that calculates how many cans of cat food you need to feed 10 cats

#Your will need:

#A variable for the number of cats
#A variable for the number of cans each cat eats in a day
#A print() function to output the result
#Extension: change the calculation to work out the amount needed for 7 days

cats = 10
cans = 2

total_cans = cats * cans

output = str(cats) + " cats eat " + str(total_cans) + " cans"
print(output)