# TODO
# write tests for the list

def divisible(num, denominator):
    if denominator == 0:
        return ZeroDivisionError 
    return ((num % denominator) == 0)

def fizzBuzz(bottom, top, trigger1, trigger2):
    if (trigger1 == 0) or (trigger2 == 0):
        return ZeroDivisionError
    result = []
    for i in range(bottom,(top+1)):
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
    

    
