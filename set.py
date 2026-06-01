#creating a set (using curly braces)
int_set={12,6,7,9,11,10}                  #set of integers
print(int_set)
str_set={"one","two","three","four"}      #set of strings
print(str_set)
mixed_set={12,"Anchal",7.2,True}          #mixed set
print(mixed_set)



#creating a set using set() function
int_list=[6,6,1,3,7,10,4]    #given list of integers
int_set=set(int_list)
print("Set1:",int_set)
empty_set=set()              #creating a empty list
print("Set2:",empty_set)


#Accessing element in a set
set={10,20,30,40}              #using for loop
for i in set:
    print(i)

set={10,20,30}
print(20 in set)              #using membership operator(in)

set={10,20,30}
print(set.pop())              #using pop()


#set methods
set={10,20,30}
set.add(40)                #add()
print(set)
set.update([50,60])        #update()
print(set)
set.remove(20)             #remove()
print(set)
set.discard(70)            #discard()
print(set)
set.pop()                  #pop()
print(set)
set2=set.copy()            #copy()
print(set2)
set.clear()                #clear()
print(set)

set_A={1,2,3}
set_B={3,4,5}
print(set_A.union(set_B))             #union()

set_A={1,2,3}
set_B={2,3,4}
print(set_A.intersection(set_B))     #intersection()

print(set_A.difference(set_B))       #difference()

set_A={1,2}
set_B={1,2,3,4}
print(set_A.issubset(set_B))         #issubset()

set_A={1,2,3,4}
set_B={1,2}
print(set_A.issuperset(set_B))       #issuperset()



