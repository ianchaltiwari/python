#defining a function
def welcome():
    print("Hello,users! Welcome")
welcome()         #calling a function


#function parameters and arguments
def welcome(name):
    print("Hello,", name, "! Welcome")

welcome("John")

#types of arguments in python
def student(name,age):
   print(name,age)

student("Anchal",22)      #positional argument 

def greet(name="Guest"):
    print("Hello",name)
greet()
greet("Anchal")           #default argument

def student(name,age):
    print(name,age)
student(age=22,name="Anchal")   #keyword argument

def add (*numbers):
    print(numbers)
add(10,20)                    #variable length argument (*args)
add(10,20,30,40)

def details(**info):
    print(info)

details(name="Anchal", age=22, city="Varanasi")


#Returning values from functions
def add(a,b):
    return a+b          #returning a single value that is the sum of two numbers
result=add(3,5)
print("The sum is",result)

def calculate(a,b):
    return a+b,a-b     #returning multiple value that is sum and difference
sum_result,diff_result=calculate(10,4)
print("Sum:",sum_result,"  ""Difference:",diff_result)


#Scope of variable in function
x = 10      # global variable

def my_function():
    y = 5   # local variable
    print("Inside function:", "x=", x, "y=", y)

my_function()

print("Outside function:", "x=", x)