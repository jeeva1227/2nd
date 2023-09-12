def FizzBuzz(n):
    i =0 
    if (n%3 ==0 and n%5 ==0 ):
        return "FizzBuzz"
    elif(n%3 ==0):
        return "Fizz"
    
    elif(n%5 == 0):
        return "Buzz"
    
    else:
        return i

n = int(input("enter: "))
output = FizzBuzz(n)
print(output)