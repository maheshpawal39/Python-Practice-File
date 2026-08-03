
# moive ticket analysir
Name = input("Enter your Name : ")
age = int(input("Enter your age : "))
day = input("Enter Today's Day : ")

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2
print("==============================================")
print(f" Wow 🥰 The price of {Name}'s Today's Ticket is 🎉 : {price}")
