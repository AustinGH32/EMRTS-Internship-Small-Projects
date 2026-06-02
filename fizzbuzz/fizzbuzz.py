#********************************************************************************************#
# FizzBuzz Project Instructions                                                              #
# Create a program that prints each number from 1 to 100 on a new line.                      # 
# For each multiple of 3, print "Fizz" instead of the number.                                #
# For each multiple of 5, print "Buzz" instead of the number.                                #
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.   #
#                                                                                            #
# This code checks for multiples of 15, 5, and 3 in that order to ensure the correct output  #
# for each case.                                                                             #
#                                                                                            #
#********************************************************************************************#


#defining the range up to 100
for x in range(1,101):
    #checking for numbers that are multiples of 3 and 5
    if x%15 == 0:
        print("FizzBuzz")
    #checking for numbers that are multiples of 5 and then 3  
    elif x%5 == 0:
        print("Buzz")
    elif x%3 == 0:
        print("Fizz")
    #printing everything else
    else:
        print(x)
