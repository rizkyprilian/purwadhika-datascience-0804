def isPrime(num):
    if num <= 3 and num > 1:
        return True
    
    for pembagi in range(2,num-1):
        if num % pembagi == 0:
            return False
    
    return True
    
def fizzbuzz(n):
    for x in range(1, n+1):
        if x == 1:
            print(x)
        elif isPrime(x):
            print('fizzprime')
        elif x%15 == 0:
            print('fizzbuzz')
        elif x%3 == 0:
            print('fizz')
        elif x%5 == 0:
            print('buzz')
        else:
            print(x)

fizzbuzz(30)


# print(isPrime(2))
# print(isPrime(3))
# print(isPrime(4))
# print(isPrime(5))
# print(isPrime(6))
# print(isPrime(7))
# print(isPrime(17))
