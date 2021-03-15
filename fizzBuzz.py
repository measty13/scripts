for i in range(1,20):
    fizz = (i % 3 == 0)
    buzz = (i % 5 == 0)
    if (fizz == False and buzz == False):
        print(i)
    elif (fizz == True and buzz == False):
        print("Fizz")
    elif (fizz == False and buzz == True):
        print("Buzz")
    else: print("FizzBuzz")
    
    
