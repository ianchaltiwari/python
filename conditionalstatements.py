#if statement
age=int(input("Enter your age"))
if age<18:
    print("You are not eligible to vote")
    
if age>=18:
    print("You are eligible to vote")
if age>=21:
    print("You are allowed to consume alcohol in some countries")
if age>=60:
    print("You are eligible for senior citizen benefits")
if age>=80:
    print("You are very senior citizen take care of your health")      

#if else statement
age=int(input("enter your age"))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")    

#another example (WAP to check if a number is a multiple of 7 or not)
number=int(input("enter the number"))
if number%7==0:
    print("multiple of 7")
else:
    print("not multiple of 7")    

#nested if else statement(program for checking if a student pass with Distinction or not)
marks=int(input("Enter your marks"))
if marks>=40:
    if marks>=75:
        print("Congratulations !! You passed with distinction")
    else:
        print("you have passed the exam")
else:
    print("You failed the exam")                

#if...elif...else statement
light=str(input("which light is blinking :"))
if light=="red":
    print("You need to stop")
elif light=="green":
    print("You can go")
elif light=="yellow":
    print("You need to wait")
else:
    print("light is broken")       

#grade students based on marks
marks=int(input("Enter your marks"))
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
print("Grade of the student=",grade)                         

