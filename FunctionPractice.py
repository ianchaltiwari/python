#sum of two number program using function
def calc_sum(a,b):
    return a+b
sum=calc_sum(17,22)
print(sum)

#Average of three number program using function
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
calc_avg(1,2,3) 

#WAF to print the length of the list(list is the parameter)
def print_length(my_list):
    print("Length of the list is:", len(my_list))

numbers = [10, 20, 30, 40, 50]

print_length(numbers)

#WAF to print the elements of a list in a single line(list is the parameter)
def print_list(my_list):
    for item in my_list:
        print(item, end=" ")

numbers = [10, 20, 30, 40, 50]

print_list(numbers)

#WAF to find the factorial of n (n is the parameter)
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

result = factorial(5)
print("Factorial =", result)

#WAF to convert US dollar to Indian rupee
def usd_to_inr(dollar):
    rupees = dollar * 86
    print("Indian Rupees =", rupees)

usd_to_inr(10)

"""write a function to input a number if no is odd then the function should return 
string odd and if the no is even the function should return string even"""

def check_number(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))

result = check_number(number)
print(result)