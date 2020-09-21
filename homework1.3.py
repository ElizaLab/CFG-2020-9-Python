# psudo code
# write in english what you want to do
# break things down to granular level

# I want to calculate N# of omolets I can make
# each carton has 6 eggs
carton_n_eggs = 6
#each omelette take 4 eggs
n_eggs_per_omeltte = 4
n_of_cartons_in_fridge = 6

#logic where we calculate number of omeletts
# first I want the total number of eggs
total_eggs = carton_n_eggs * n_of_cartons_in_fridge
#print(total_eggs)
# then I want to dived by 4 to get the total amout I can make
total_omeletts = total_eggs / n_eggs_per_omeltte
#print(total_omeletts)
# in the end I want it to print the number of omelettes I can make. Something like:
print("You can make {} omelettes with {} boxes of eggs".format(total_omeletts, n_of_cartons_in_fridge ))