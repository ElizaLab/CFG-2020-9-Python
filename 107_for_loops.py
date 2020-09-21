# For loops
# this are great to do 1 task a lot of times!

#syntax
# for <item> in <iteratable>:
    # block of code
    # set of instruction that get repeated


cringy_peeps = ['Cristina', "john", "Doe", "Mad Max"]

#print("Go take a hike " + cringy_peeps[0])
#print("Go take a hike " + cringy_peeps[1])

##--->>> introducing FOR LOOPS!
cringy_peeps = ['Cristina', "john", "Doe", "Mad Max"]

for peep in cringy_peeps:
    #print(peep)
    print("yay")
    print("Go take a hike " + peep)

for num in range(10):
    print(num)