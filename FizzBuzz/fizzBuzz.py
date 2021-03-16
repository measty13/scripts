def divisible(num, denominator):
	return ((num % denominator) == 0)

def fizzBuzz(top, trigger1, trigger2):        
    for i in range(1,(top+1)):
        fizz = divisible(i, trigger1)
        buzz = divisible(i, trigger2)
        if (fizz == False and buzz == False):
            print(i)
        elif (fizz == True and buzz == False):
            print("Fizz")
        elif (fizz == False and buzz == True):
            print("Buzz")
        else: print("FizzBuzz")

    
