# 1 even or odd

# user=int(input("enter a number: "))
# if user>0:
#     if user%2==0:
#         print("it is odd")
#     else:
#         print("it is a odd number")
# else:
#     print("its negative number")        

# 2 Vowel Counter

# string=input("enter a string:")
# count=0
# for i in string:
#  if i in "AEIOUaeiou":
#     count+=1
# print("vowels:",count)

# 3 Print Squares

# for i in range(1,11,1):
#     print(i,"*2",":",i**2)

# 4 Countdown using while loop

# num=10
# while num>=1:
#     print(num)
#     num-=1

# 5 Sum of Even Numbers 1-100

# summ=0
# for i in range(1,101):
#     if i%2==0:
#         summ+=i
# print(summ)

# 6 Tuple Search

# number=(12,23,45,67,87,54)

# user=int(input("enter a number:"))
# if user in number:
#     print("number found.")
# else:
#     print("number Not found.")

# 7. Fruit List

# fruits=["apple","banana","carrot","orange"]
# user=input("enter a fruit:")
# fruits.insert(1,user)
# fruits.pop()
# print(fruits)

# 8 Dictionary Access

# person = {
# "name": "Rahul",
# "age": 25,
# "city": "Kochi"
# }

# x=person.get("age")
# print("age:",x)
# person.pop("city")
# person["profession"]=input("enter a job:")
# print(person)

# 9 Skip Negative Numbers

# number=[23,45,67,87,-67,44,-67,-21]
# for i in number:
#     if i<0:
#         continue
#     print(i)

# 10 Count Characters

# string=input("enter a string:")
# count=0
# for i in string:
#     if i.isalpha():
#         count+=1
# print("count:",count)

# 11 Simple Billing System

# cart=[]
# for i in range(5):
#     user=int(input("enter rate:"))
#     cart.append(user)

# total=sum(cart)
# print("total:",total)
# if total>5000:
#     discount=total*10/100
#     after_dicount=total-discount

#     print("price after dicount",after_dicount)

# 12 Password Validation

ps=input("ENTER PASSWORD:")
count=0
for i in ps:
    if i in "0123456789":
        count+=1
if len(ps)>=8 and count>0:
    print("valid password")
else:
    print("invalid password")
