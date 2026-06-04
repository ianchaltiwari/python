#print number from 1 to 5
i=1
while i<=5:
    print(i)
    i+=1

#print reverse (5 to 1)
i=5
while i>=1:
    print(i)
    i-=1

#use of else statement in while loop
i=1
while i<=10:
    print(i)
    i+=1
else:
    print("loop completed successfully")


#using break
i=1
while i<=10:
    if i==5:
        break
    print(i)
    i+=1
else:
    print("loop completed successfully")


#Find the multiplication table of a number n
n=int(input("Enter number"))
i=1
while i<=10:
    print(n*i)
    i+=1


#print the element of the following list using while loop
nums=[1,4,9,16,25,36,49,64,81,100]
idx=0
while idx<len(nums):
    print(nums[idx])
    idx+=1        


#search for a number x in this tuple using while loop
tuple=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0
while i<=len(tuple):
    if(tuple[i]==x):
        print("found at index",i)
        break
    i+=1

#print only even number from 1 to 10
i=1
while i<=10:
    if i % 2 ==0:
        print(i)
    i+=1         


#print only odd number from 1 to 10
i=1
while i<=10:
    if i % 2!=0:
        print(i)
    i+=1    


#print sum of first five natural number
i=1
sum=0
while i<=5:
    sum=sum+i
    i+=1
print("Sum=",sum)
    

#print factorial of number
n=3
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("Factorial=",fact)        
