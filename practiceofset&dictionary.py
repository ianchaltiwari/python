"""Store following word meanings in a python dictionary:
table: "a piece of furniture" , "list of facts and figures"
cat: "a small animal"""

Dictionary={
    "table": ["a piece of furniture","list of facts and figures"],
    "cat":"a small animal"
}
print(Dictionary)


"""You are given a list of subjects for students.Assume one classroom is required for 1 subject
how many classrooms are needed by all the students.
[python,java,C++,python,javascript,java,python,java,C++,C]"""

set_subjects={
    "python","java","c++","python","javascript","java",
    "python","java","c++","c"
}
print(len(set_subjects))


"""WAP to enter marks of three subjects from the user and store them in a dictionary.Start with an empty dictionary and add one 
by one.Use subject name as key and marks as value"""

marks={}
x=int(input("Enter phy:"))
marks.update({"phy":x})
x=int(input("enter math:"))
marks.update({"math":x})
x=int(input("enter chem:"))
marks.update({"chem":x})
print(marks)


"""Figure out a way to store 9 & 9.0 as separate values in the set
(you can take help of built in data types)"""

#first way
values={
    ("floiat",9.0),
    ("int",9)
}
print(values)

#second way
values={9,"9.0"}
print(values)
