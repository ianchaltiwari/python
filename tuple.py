#creating a tuple
tuple=(10,20,30)
print(tuple)
tuple=(1,"Anchal",3.5)    #tuple consisting of multiple datatypes
print(tuple)
tuple=(5,)                #tuple consisting of single element
print(tuple)
print(type(tuple))

#Indexing in tuple
tuple=("Apple","Mango","Banana","Guava","Berries")
print(tuple[0])
print(tuple[2])
print(tuple[-1])
print(tuple[-2])

#Slicing in tuple
t=(10,20,30,40,50,60)
print(t[1:4])
print(t[:3])
print(t[2:])
print(t[-4:-1])

#Tuple methods
t=(1,2,2,3,2)
print(t.count(2))    #count()

t=(10,20,30,20)
print(t.index(20))

#WAP to count the number of students with the "A" grade in the following tuple
grade=("C","D","A","A","B","B","A")
print(grade.count("A"))



