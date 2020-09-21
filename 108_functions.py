# Functions
# should have 1 job! and do it well
# if a variable is box, then a function is like a machine!
    # 1) it take in inputs AKA: arguments
    # 2) , does something AKA: block of code
    # 3) output the results - with return!

# it helps you not have to repeat yourself
#syntax
#def <name_funtion>(arg1, arg2):
    # block of code
    # block of code come after a : and are indented
    # return result

# arguments exist withing the scope of the function

#1)Define a function that constructs a full name with two arguments

def full_name(first_n, last_n):
    complete_name = first_n + " " +last_n
    print(complete_name)

# 2) call the function with data for the argument

full_name('Li', "Stark") #calling function with two strings

student_f_name = input("what is your first name")
student_l_name = input("what is your last name")

full_name(student_f_name, student_l_name)

