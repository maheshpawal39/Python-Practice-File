password = input("Enter yoyr password length: ")

if len(password) < 6:
    print("password is week")
elif len(password) <=10 :
    print("password is Medium")
else:
    print("password is strong")    
