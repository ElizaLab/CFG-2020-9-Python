# burger exercise

#ask user for input
price_burger = int(input('what is the price of the burger').strip())

#check if less than 10
is_less_than_10 = price_burger <= 10
# print that restaurant is within budget
print("your option is with in budget:" + str(is_less_than_10))

#ask user for input
option_has_vegan = input("is there a vegan option(y/n)").strip()
#check if restaurant has a vegan option
has_vegan = option_has_vegan == 'y'

print("your option has a vegan menu:" + str(has_vegan))

# print that restaurant is within BOTH criteria
#check if meets the two criteria
meets_both_criteria = has_vegan and is_less_than_10
#print(meets_both_criteria)

print("your option has a vegan menu AND is less than 10pounds: " + str(meets_both_criteria))


# we want to use if condition
# in this program , if it's less than 10 and Vegan,
    # then it's a good option
# else we need to keep searching