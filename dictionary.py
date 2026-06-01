#creating a dictionary
Dictionary={1:"Learn",
            2:"Python",
            3:"With",
            4:"Me"}
print(Dictionary)


#creating another dictionary 
dict_zero={}
dict_one={"name":"Lucy",
          "age":19,
          "country":"UK"}
dict_two=dict(name="John",age=21,country="Havana")  #using dict_one()
print("empty dictionry:",dict_zero)
print("Dictionary1:",dict_one)
print("Dictionary2:",dict_two)


#accessing dictionary items
dict_x={
    "name": "Sachin",
    "age":18,
    "gender":"Male",
    "profession":"Student"
}
print("Person's details:")
print("Name:",dict_x["name"])  #accessing dictionary items using keys
print("Age",dict_x["age"]) 

print("Gender",dict_x.get("gender"))    #accessing dictionary items using get()
print("profession",dict_x.get("profession"))



#Dictionary methods
student={
    "name":"Anchal",
    "age":22,
    "City":"Varanasi"
}
print(student.keys())                #key()
print(student.values())              #values()
print(student.items())               #items()
print(student.get("age"))            #get()
student.update({"phone":9876523870})#update()
print(student)   
print(student.pop("City"))           #pop()
student2=student.copy()              #copy()
print(student.copy())
students=["Aman","Riya","Anchal"]
d=dict.fromkeys(students,0)
print(d)
student.clear()
print(student)


#nested dictionary
students={
    101:{
        "name":"Anchal",
        "age":22
    },
    102:{
        "name":"Riya",
        "age":23
    }
}
print(students)