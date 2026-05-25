#arithmetic operators
a=5
b=2
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)

#comparison operators
a=50
b=20
print(a==b)
print(a!=b)
print(a>=b)
print(a>b)
print(a<=b)
print(a<b)

#Assignment operators
num=10
num+=10
print(num)

#bitwise operators
a=5
b=3
print(a & b) #bitwise and
print(5|3)   #bitwise or
print(5^3)    #bitwise xor
print(~5)     #bitwise not
print(5<<1)   #left shift
print(5>>1)   #right shift

#logical operators
a=10
b=5
print(a>5 and b>2)
print(a>20 or b>2)
print(not(a>5))

#membership operators
list=(100,200,300)
print(200 in list)       #in operator
print(500 not in list)   #not in operator

#identity operators
a=10
b=10
print(a is b)      #is operator
a=10
b=20
print(a is not b)  #is not operator