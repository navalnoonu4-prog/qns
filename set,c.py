# 1 

# user=int(input("Enter Your age:"))
# if user<13:
#     print("Child")
# elif user>13 and user<=19:
#     print("Teenager")
# elif user>20 and user<60:
#     print("Adualt")
# else:
#     print("Seniour Citizen")

# 2 Multiple of 3 or 5

# user=int(input("enter a number:"))
# if user%3==0 and user%5==0:
#     print(user," is a multiple of 3 and 5")
# else:
#     print(user," not multiple of 3 and 5")

# 3 Print Odd Numbers 

# for i in range(1,51,2):
#     print(i)

# 4 Multiplication Table

# user=int(input("enter a number:"))
# for i in range(1,11,1):
#     print(i,"x",user,":",i*user)

#5 Count Digits

# count=0
# string=input("enter a string:")
# for i in string:
#     if i.isdigit():
#         count+=1
# print(count,"Digits")

# 6 Find Second Largest

# number=(23,45,67,43,21,56)
# largest=max(number)
# num=list(number)
# num.remove(largest)
# second=max(num)
# print("second Largest:",second)


# 7 List of Movies

# movies=["iam game","bku","khalifa","dc","toxic"]
# print("first Movie:",movies[0])
# print("last Movie:",movies[-1])
# movies[1]="paradise"
# print(movies)

# 8 Dictionary Marks

# student={
#     "naval":90,
#     "fayis":78,
#     "amraz":90
#     }

# print(student)

# student["liya"]=60
# print(student)

# del student["fayis"]
# print(student)


# 9 Break Statement

# for i in range(1,21,1):
#     if i==13:
#         break
#     print(i)

# 10 Sum of List Elements using Lopp

# numbers=[23,45,67,89,65,45,67,12,32]
# total=0
# for i in numbers:
#     total+=i
# print(total)

# 11 ATM Withdrawal System.

# balance=10000

# try:

#  amount=int(input("enter amount to withdraw: "))
#  if amount<0:
#   print("Amount will be Positive only")
#  elif amount>balance:
#   print("insufficient Balance")
#  else:
#   print("withrawal Succesfull")
#   balance-=amount
#   print("remaining balance:",balance)

# except ValueError:
#  print("invalid Input.Please Enter a number")

# 12 Student Grade Function

# def  calc_marks(m1,m2,m3,m4,m5):
#     total=m1+m2+m3+m4+m5
#     avg=total/5

#     if avg>90:
#         grade="A"
#     elif avg>75:
#         grade="B"
#     elif avg>60:
#         grade="C"
#     elif avg>50:
#         grade="D"
#     else:
#         grade="F"

#     return total,avg,grade
    
# m1=int(input("Enter mark:"))
# m2=int(input("Enter mark:"))
# m3=int(input("Enter mark:"))
# m4=int(input("Enter mark:"))
# m5=int(input("Enter mark:"))

# total,avg,grade=calc_marks(m1,m2,m3,m4,m5)
# print("total:",total)
# print("average:",avg)
# print("grade:",grade)

# 13 Unique list program

# numbers = [10, 20, 10, 30, 20, 40, 50, 30]
# num=set(numbers)
# uniq=list(num)
# order=sorted(uniq)
# print("unique Numbers:",order)
# print("number of unique elements:",len(uniq))

# 14 Inventory Dictionary

# inventory = {
# "apple": 10,
# "banana": 20,
# "orange": 15
# }

# inventory["melonn"]=40
# inventory["banana"]=35
# del inventory["orange"]
# for i,n in inventory.items():
#  print(i,":",n)

# 15 Menu-Driven Calculator with Exception Handling


# try:
#  while True:
#     print("--CALCULATOR--")
#     print("1. Addition")
#     print("2. subtraction")
#     print("3. multiplication")
#     print("4. Division")
#     print("5. Exit")
#     ch=int(input("enter a choice(1-5):"))

#     if ch==1:
#         n1=int(input("enter first Num:"))
#         n2=int(input("enter second num:"))
#         total=n1+n2
#         print("Total:",total)
#     elif ch==2:
#         n1=int(input("enter first Num:"))
#         n2=int(input("enter second num:"))
#         sub=n1-n2
#         print("result:",sub)
#     elif ch==3:
#         n1=int(input("enter first Num:"))
#         n2=int(input("enter second num:"))
#         mul=n1*n2
#         print("Result:",mul)
#     elif ch==4:
#         n1=int(input("enter first Num:"))
#         n2=int(input("enter second num:"))
#         try:
#             div=n1/n2
#             print("result:",div)
#         except ZeroDivisionError:
#             print("division By zero Not allowed")
#     elif ch==5:
#         print("Programm Closed")
#         break
# except ValueError:
#     print("invalid Input")  

# 16  Student Report Dictionary

student = {}
student["name"]=input("enter student name: ")
student["age"]=int(input("enter age:"))
student["course"]=input("enter course :")

marks=[]
for i in range(5):
    mark=int(input("enter marks: "))
    marks.append(mark)
student["marks"]=marks

total=sum(marks)
average=total/len(marks)
highest=max(marks)
lowest=min(marks)

student["total"]=total
student["average"]=average
student["highest mark"]=highest
student["lowest mark"]=lowest

avg=student["average"]
if avg>90:
    Grade="A"
elif avg>75:
    Grade="B"
elif avg>60:
    Grade="c"
elif avg>50:
    Grade="D"
else:
    Grade="F"
student["grade"]=Grade

if avg>50:
    result="pass"
else:
    result="fail"
student["result"]=result

print("student details")
for key,value in student.items():
    print(key,":",value)


      