#creating a string
str="Anchal"
print("String:",str)
print("DataType",type(str))

#creating string with single quotes
str1='Anchal'
print("String1:",str1)

#creating string with triple quotes i.e. multiline string creation
str2="""Learning python is fun
python programming is easy  """
print("Multiline string:",str2)

#indexing in String
str3="Anchal Tiwari"
ch=str[0]
print(str[0])

#Slicing in string
str3="Anchal Tiwari"
print(str3[1:4])
print(str3[:4])
print(str3[5:])

#negative indexing in python
str4="Apple"
print(str4[-3:-1])

#string functions
name="python"
print(name.upper())   #upper()

name="PYTHON"
print(name.lower())   #lower()

name="python"
print(name.capitalize())  #capitalize()

name= "   Python   "
print(name.strip())        #strip()

text="I like Java"
print(text.replace("Java","Python"))  #replace()

name="Python"
print(name.find("t"))     #find()

text="Apple"
print(text.count("p"))  #count()

text="Python Java C"
print(text.split())      #split

name="Python"
print(len(name))        #len()

#WAP to input user's first name and print its length

name=input("Enter your name")
print("Length of name is=",len(name))






