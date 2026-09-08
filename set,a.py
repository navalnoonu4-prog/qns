# 1. POSITIVE NEGATIVE ZERO NUMBER

# user=float(input("enter a number:"))
# if user<0:
#     print(user,"is negative number")
# elif user==0:
#     print(user,"is zero")
# else:
#     print(user,"number is positive")

# 2. VOWEL OR CONSONENT

# user=input("enter a words: ")
# if user in "aeiouAEIOU":
#     print(user,"is vowel")
# else:
#     print(user,"is consonent")

# 3. EVEN OR ODD

# user=int(input("enter a number: "))
# if user%2==0:
#     print(user,"is even number")
# else:
#     print(user,"is odd number")

# 4. SUM OF EVEN NUMBERS

# sum=0
# for i in range(1,51):
#     if i%2==0:
#         sum+=i
# print(sum)

# 5 MULTIPLICATION TABLE

# user=int(input("enter number: "))
# for i in range(1,11):
#     print(i,"x",user,"=,i*user)

# 6. COUNT VOWELS

# count=0
# user=input("enter a word: ")
# for i in user: 
#     if i in "aeiouAEIOU":
#      count+=1
# print(count)

# 7 LIST OPRERATIONS

# fruits=["apple","banana","carrot","orange","melon"]
# fruits.append("water")
# fruits.insert(2,"kiwi")
# fruits.pop()
# print(fruits)

# 8 TUPLE OPERATION

# number=(1,5,7,45,34)
# print(len(number))
# print(min(number))
# print(max(number))

# 9 COUNT UPPER CASE LOWER CASE

# upper=0
# lower=0
# user=input("enter a string: ")
# for i in user:
#     if i.isupper():
#         upper+=1
#     elif i.islower():
#         lower+=1
# print("number of lower keys",lower)
# print("number of upper keys",upper)

# 10 SKIP MULTIPLE OF 3

# for i in range(0,31):
#  if i%3==0:
#   continue
#  print(i)

# 11 STUDENT RESULT

# marks=[]
# for i in range(5):
#     i=int(input("enter marks:"))
#     marks.append(i)
# # print(marks)
# total=sum(marks)
# average=total/len(marks)
# print("total marks",total)
# print("average marks",average)

# if average>90:
#     print("grade A")
# elif average>75 and average<89:
#     print("grade B")
# elif average>60 and average<74:
#     print("grade c")
# elif average>50 and average<59:
#     print("grade D")
# elif average<50:
#     print("fail")
# if average>50:
#     print("pass")

# 12. ATM MENU PROGRAM

# balance=5000
# while True:
#     print(1,"check balance")
#     print(2,"deposit money")
#     print(3,"withdraw")
#     print(4,"exit")
#     ch=int(input("enter a choice(1-4): "))
#     if ch==4:
#         break
#     elif ch==1:
#         print("balance:" ,balance)
#     elif ch==2:
#         user=int(input("enter amount to deposit: "))
#         balance+=user
#         print("available balance:" ,balance)
#     elif ch==3:
#         n1=int(input("enter amount to withdraw: "))
#         if n1>balance:
#             print("insufficient balance")
#         else:
#             balance-=n1
#             print("remaining balance:" ,balance)

# 13 LOGIN SYSTEM

# password="python123"
# for i in range(3):
#  user=input("enter password:")
#  if user==password:
#   print("login succesfull")
#   break
#  else:
#   print("login unsuccedsfull")

# 14 LIST ANALYSIS

# number=[10,15,20,25,30,25,40]
# count=0
# even=[]
# odd=[]
# for i in number:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
#     if i%5==0:
#         count+=1
# print("Even Numbers are: ",even)
# print("odd Numbers are: ",odd)
# print("sum of even numbers are :",sum(even))
# print("multiple of 5s :",count)

# 15 ,MENU DRIVEN TUPLE PROGRAM

# numbers=(12,23,45,67,23,16,17,23,90,98)
# while True:
#     print(1,"display tuple")
#     print(2,"find length")
#     print(3,"search an element")
#     print(4,"count an element")
#     print(5,"find the sum of even numbers")
#     print(6,"find the second largest numbers") 
#     print(7,"exit")
#     ch=int(input("enter a choice (1-7): "))
    
#     if ch==7:
#         break
#     elif ch==1:
#         print("numbers:",numbers) 
#     elif ch==2:
#         print("length of tuple:",len(numbers))
#     elif ch==3:
#         user=int(input("enter a number: "))
#         if user in numbers:
#             print("number found")
#     elif ch==4:
#         n1=int(input("enter a number:"))
#         count=numbers.count(n1)
#         print("count:",count)
#     elif ch==5:
#         summ=0
#         for i in numbers:
#             if i%2==0:
#                 summ+=i
#         print("sum of even numbers:",summ)
#     elif ch==6:
#         largest=max(numbers)
#         num1=list(numbers)
#         num1.remove(largest)
#         second=max(num1)
#         print("second largest Number:",second)
#     else:
#         print("enter choice (1-7)")

# 16 Student Management and Result System

# student = {}
# student["name"]=input("enter student name: ")
# student["age"]=int(input("enter age:"))

# marks=[]
# for i in range(5):
#     mark=int(input("enter marks: "))
#     marks.append(mark)
# student["marks"]=marks

# total=sum(marks)
# average=total/len(marks)
# highest=max(marks)
# lowest=min(marks)

# student["total"]=total
# student["average"]=average
# student["highest mark"]=highest
# student["lowest mark"]=lowest

# avg=student["average"]
# if avg>90:
#     Grade="A"
# elif avg>75:
#     Grade="B"
# elif avg>60:
#     Grade="c"
# elif avg>50:
#     Grade="D"
# else:
#     Grade="F"
# student["grade"]=Grade

# if avg>50:
#     result="pass"
# else:
#     result="fail"
# student["result"]=result

# print("student details")
# for key,value in student.items():
#     print(key,":",value)
        
          


