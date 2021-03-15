def divisible(num, denominator):
	return ((num % denominator) == 0)


for i in range(1,20):
    fizz = divisible(i, 3)
    buzz = divisible(i, 5)
    if (fizz == False and buzz == False):
        print(i)
    elif (fizz == True and buzz == False):
        print("Fizz")
    elif (fizz == False and buzz == True):
        print("Buzz")
    else: print("FizzBuzz")

    
