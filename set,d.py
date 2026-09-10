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

# ps=input("ENTER PASSWORD:")
# count=0
# for i in ps:
#     if i in "0123456789":
#         count+=1
# if len(ps)>=8 and count>0:
#     print("valid password")
# else:
#     print("invalid password")

# 13 Number List Processor

# numbers=[]
# for i in range(10):
#     n=int(input("enter number:"))
#     numbers.append(n)
# positive=[]
# negative=[]
# even=[]
# odd=[]
# for x in numbers:
#     if x>0:
#         positive.append(x)
#     elif x<0:
#         negative.append(x)
#     if x%2==0:
#         even.append(x)
#     else:
#         odd.append(x)
# print("positive Numbers:",positive)
# print("Negative Numbers:",negative)
# print("Even Numbers:",even)
# print("ODD numbers:",odd)

# 14 Tuple Student Marks

# marks=(34,56,78,56,45)

# count=0
# print("total Marks:",sum(marks))
# print("Average:",sum(marks)/len(marks))
# print("highest marks:",max(marks))
# print("Lowest mark:",min(marks))

# for i in marks:
#     if i>=75:
#         count+=1
# print("student above 75 Marks:",count)

# 15 Bus Ticket Booking System

# available=5
# booked=0

# while True:
#     print("1. View available Seats.")
#     print("2. Book ticket.")
#     print("3. Cancel Ticket")
#     print("4. exit")
#     ch=int(input("Enter your choice(1-4): "))
    
#     if ch==1:
#         print("Available seats:",available)
#     elif ch==2:
#         if available>0:
#             available-=1
#             booked+=1
#             print("Booking Confirmed..")
#             print("Remaining seats:",available)
#         else:
#             print("no seats available...")

#     elif ch==3:
#         if booked>0:
#             booked-=1
#             available+=1
#             print("Ticket cancelation Confirmed..")
#             print("remaining seats:",available)
#         else:
#             print("cancelation Not available...")        
#     elif ch==4:
#         print("thank your for your booking...")
#         break
#     else:
#         print("invalid input")
        

# 16 Online Shopping Cart

products = {
"Laptop": 50000,
"Phone": 20000,
"Mouse": 1000
}

cart={}
while True:
    print("--Shoping Cart--")
    print("1. add product")
    print("2. Remove product")
    print("3. View cart")
    print("4. Total")
    print("5. exit")
    ch=int(input("enter your choice(1-5):"))
    if ch==1:
       print("available products")
       print(products)

       name=input("enter product name:")
       if name in products:
           cart[name]=products[name]
           print("Added to cart")
       else:
           print("Product Not available")

    elif ch==2:
        name=input("enter product to remove:")
        if name in cart:
            del cart[name]
            print("Product removed..")

    elif ch==3:
        for product,rate in cart.items():
            print(product,":",rate)
    elif ch==4:
        total=0
        for price in cart.values():
            total+=price
        print("Total amount:",total)

    elif ch==5:
        print("Thank You for shopping..")
        break
    else:
        print("Invalid choice")


