marks = int(input("Enter your makrs : "))

if marks >= 101:
    print("Plz Verify Your marks 'again' ")
    exit()

elif marks >= 90:
    Grade = "A"
    
elif marks >= 80:
    Grade = "B"

elif marks >= 70:
    Grade = "C"

elif marks >= 60:
    Grade = "D"

else :
    Grade = "F"    

print("Grade" , Grade)