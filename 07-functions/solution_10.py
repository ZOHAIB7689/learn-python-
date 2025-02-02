# create  recursive function to calculate  the factorial of the number

def factorial(n):
    if n == 0 :
        return 1 
    else: 
        return n  * factorial(n-1)
    
print(factorial(12))