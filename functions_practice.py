# A function named hello() that prints greeting to the user.This function shuold accept no arguements and return nothing

def hello():
    print("Hello, user!")

hello()

# A function named pack() that accepts three arguments, and return a single list with the three arguements inside as list elements

def pack(x,y,z):
    return [x,y,z]

print(pack("a","b","c"))
print(pack(1,2,3))

# A function called eat_lunch(). This function should accept a list of any length, and print out a series of strings that say "First I eat__"(the first element of the list), and 
# "Next I eat __"(for the following element in the list).If the list is empty, print "My lunchbox is empthy!".
# The function shuold not return anything. 

def eat_lunch(my_list):
    if len(my_list) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(my_list)):
            if i == 0:
                print(f"First I eat {my_list[0]}")
            else:
                print(f"Next I eat {my_list[i]}")

eat_lunch([])
eat_lunch(["pizza"])
eat_lunch(["apple","banana","pizza","cupcake"])