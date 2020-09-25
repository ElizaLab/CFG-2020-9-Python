
#ask user for input
price_burger = int(input('what is the price of the burger').strip())
#ask for vegan option
option_has_vegan = input("is there a vegan option(y/n)").strip()

# we want to use if condition
# in this program , if it's less than 10 and Vegan,
if price_burger <= 10 and option_has_vegan == 'y':
    print(" it's a good option")
    # then it's a good option
# else we need to keep searching
else:
    print("we need to keep searching")