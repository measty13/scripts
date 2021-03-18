# TODO
# write tests for the list

def divisible(num, denominator):
	return ((num % denominator) == 0)

def fizzBuzz(top, trigger1, trigger2):
    result = []
    for i in range(1,(top+1)):
        fizz = divisible(i, trigger1)
        buzz = divisible(i, trigger2)
        if (fizz == False and buzz == False):
            result.append(i)
        elif (fizz == True and buzz == False):
            result.append("Fizz")
        elif (fizz == False and buzz == True):
            result.append("Buzz")
        else:
            result.append("FizzBuzz")
    return result
    

    
