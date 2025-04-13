x=int(input("Enter a number :"))

def fact(x):
    if x<2:
        return 1
    else:
        return x * fact(x-1)

result=fact(x)
print(f" Factorial of {x} is :",result)