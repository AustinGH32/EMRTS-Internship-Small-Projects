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
