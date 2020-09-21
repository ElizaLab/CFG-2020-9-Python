# List
# list behave like list in normal life, you can keep  list of this
# syntax --> how to write it in python
    # []
print(type([]))
print([])

#simple list --> hold data types in order
my_list = ['egg', 'milk', 1, 2]
print(my_list)
print(type(my_list))

# example 2
cringy_peeps = ['Cristina', "john", "Doe", "Mad Max"]
print(cringy_peeps)

# 1st thing to understand is how they are organize --> index!
    # index is a way of counting that start at 0
# index      = [     0    ,  1    ,   2   ,   3     ]    #use index to access something in list
cringy_peeps = ['Cristina', "john", "Doe", "Mad Max"]

# access the firs item? --> use your list and select index 0
print(cringy_peeps[0])

# access the the second item --> use your list and select index 1
print(cringy_peeps[1])

# Change something in a list
    #1) access that item, and 2) re-assign item
print(cringy_peeps)
cringy_peeps[0] = "Diana Kyle"
print(cringy_peeps)

# add more items?
# use .append(item)
cringy_peeps.append("James")
cringy_peeps.append("Donald")
print(cringy_peeps)

# Remove last item from list? .pop()
cringy_peeps.pop()
print(cringy_peeps)

# Remove item using index? .pop(i)
cringy_peeps.pop(2)
print(cringy_peeps)



