#for loop
nums=[1,2,3,4,5]         #list sequence
for value in nums:       #print 1 to 5
    print(value)

tup=(1,2,3,4,5,6,7,8,9,10)
for num in tup:              #tuple sequence
    print(num)          

veggies=("potato","brinjal","cucumber")    #string sequence
for value in veggies:
    print(value)

str="apna college"
for char in str:
    print(char)


#for loop using range function
for i in range(5):
    print("Hello")

for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(2,11,2):
    print(i)

for i in range(1,10,2):      #printing odd numbers from 1 to 10
    print(i)

for i in range(10,0,-1):     #printing reverse counting(negative step)
    print(i)            


#Iterating by the index of sequence in for loop
fruit_basket=["apple","banana","orange","kiwi"]
for i in range(len(fruit_basket)):
    print(i,":",fruit_basket[i])


#use of else statement with for loop
for i in range(1,6):
    print(i)
else:
    print("Loop completed successfully")     #loop completes normally

for i in range(1,6):
    if i ==3:
        break                                #using break
    print(i)
else:
    print("Loop completely successfully")


#searching an element
numbers=[10,20,30,40]
search=25
for num in numbers:
    if num==search:
        print("element found")
        break
else:
    print("element not found")        


"""print the element of the following list using for loop
[1,4,9,16,25,36,49,64,81,100]"""

nums=[1,4,9,16,25,36,49,64,81,100]
for el in nums:
    print(el)



