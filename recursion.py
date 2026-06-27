#Factorial using recursion
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))


#Sum of first n natural number using recursion
def sum_n(n):
    if n==1:
        return 1
    return n+sum_n(n-1)
print(sum_n(5))