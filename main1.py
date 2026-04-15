num = int(input("The program will find the factorial of the number entered: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)
if num<0:
    print("Sorry, factorial values don't exist for this")
else:
    print(f"The factorial of that number is {factorial(num)}")