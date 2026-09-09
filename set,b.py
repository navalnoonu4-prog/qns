# 1 CHECK DIVISIBILITY

# user=int(input("enter a number:"))
# if user%3==0 and user%5==0:
#     print("divisible by both 3 and 5")
# else:
#     print("undivisible by both 3 and 5")

# 2 classification

# user=input("enter a word:")
# if user.isupper():
#     print("it is a upper case letter")
# elif user.islower():
#     print("it is a lower case letter")
# elif user.isdigit():
#     print("it is a digit")
# else:
#     print("it is a special charecter")

# 3 Reverse counting

# for i in range(20,0,-1):
#     print(i)

# 4 sum of even numbers

# n=int(input("enter a number:"))
# summ=0
# for i in range(1,n+1):
#     summ+=i
# print("sum of numbers:",summ)

# 5 string charecter display

# word=input("enter a word: ")
# for i in range(len(word)):
#     print(word[i],"=",i)

# 6 count even odd

# numbers=(12,34,56,78,54,32,45,67)
# even=0
# odd=0
# for i in numbers:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("even numbers:",even)
# print("odd numbers:",odd)

# 7 list modification

# names=["naval","fayis","amraz","shibili","liya"]
# names[2]="vinayak"
# user=input("enter a name to add:")
# names.append(user)
# names.pop(0)
# print(names)

# 8 Dictionery creation

# student={}
# student["name"]=input("enter name:")
# student["age"]=int(input("enter age:"))
# student["course"]=input("enter course:")
# student["grade"]=input("enter grade:")

# print(student)

# 9 countinue statement

# for i in range(1,21):
#     if i%4==0:
#         continue
#     print(i)

# 10 find largest

# n1=int(input("enter first number:"))
# n2=int(input("enter second number:"))

# if n1>n2:
#     print(n1,"is greatest")
# else:
#     print(n2,"is greatest")

# 11 password login

# password="admin123"
# for i in range(3):
#  user=input("enter password:")
#  if user==password:
#   print("login succesfull")
#   break
#  else:
#   print("login unsuccedsfull")

# else:
#  print("account locked")


# 12 shopping cart

# Products=[
#  ["apple",130],
#  ["banana",80],
#  ["orange",120]
# ]

# while True:
#  print(1,"display products:")
#  print(2,"add price:")
#  print(3,"total")
#  print(4,"exit")
#  ch=int(input("enter choice(1-4): "))
#  if ch==1:
#   print("Products")
#   for product in Products:
#    print(product[0],":",product[1])

#  elif ch==2:
#   name=input("enter product name:")
#   price=int(input("enter product price: "))
#   Products.append([name,price])
#   print("product added succesfully ")
#  elif ch==3:
#   total=0
#   for product in Products:
#    total+=product[1]
#   print("total :",total)
#  elif ch==4:
#   print("program closed! ")
#   break
#  else:
#   print("invalid choice")


# 13 Marks List Analysis

# marks=[]
# for i in range(5):
#     mark=int(input("enter student marks: "))
#     marks.append(mark)

# highest=max(marks)
# lowest=min(marks)
# total=sum(marks)
# average=total/len(marks)
# count=0
# for mark in marks:
#  if mark>=50:
#     count+=1

# print("highest mark:",highest)
# print("lowest mark:",lowest)
# print("total:",total)
# print("average mark:",average)
# print("number of student passed:",count)

# 14 Punctuation Remover

# user=input("enter a word:")
# name=""

# for i in user:
#     if i.isalnum():
#         name+=i
# print("output:",name)
     
# 15 Number Guessing Game

# secret=25

# for i in range(5):
#     n=int(input("Guess a Number:"))

#     if n>secret:
#         print("Too High.")
#     elif n<secret:
#         print("Too Low.")
#     elif n==secret:
#         print("Correct answer.")
#         break

# else:
#     print("Game Over.")

# 16 Restaurant Ordering System

# menu = {
# "Burger": 150,
# "Pizza": 300,
# "Juice": 80,
# "Pasta": 200
# }

# order=[]
# while True:
#     print("1. View Menu ")
#     print("2. Order Food ")
#     print("3. View Bill ")
#     print("4. Exit ")
#     ch=int(input("Enter Your Choice (1-4): "))
#     if ch==1:
#         print("---MENU----")
#         for item,price in menu.items():
#             print(item,":",price)

#     elif ch==2:
#         user=input("Select a food: ")
#         if user in menu:
#             print(user,"Order Confirmed") 
#             order.append(user)
#         else:
#             print("This food not in our Menu.")
#     elif ch==3:
#         total=0
#         print("--BILL--")
#         for user in order:
#             print(user,":",menu[user])
#             total+=menu[user]


#         print("total:",total)
#     elif ch==4:
#         print("Thank you For Ordering.")
#         break
#     else:
#         print("Invalid Choice")

            

