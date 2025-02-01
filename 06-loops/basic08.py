number = input("Enter a number: ")
number = int(number)

is_prime = True

if  number > 1 :
    for i in range(2, number):
        if number % i == 0:
            is_prime = False 
            break

if is_prime:
     print("yes", number, "is a prime number")
else: 
    print("Not a prime number")