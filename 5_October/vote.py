age=int(input("Enter age:"))
if(age>0 and age>=18 and age<=100):
    print("Eligible for vote")
elif(age>0 and age<18):
    print("Not eligible for vote")
else:
    print("not correct age")