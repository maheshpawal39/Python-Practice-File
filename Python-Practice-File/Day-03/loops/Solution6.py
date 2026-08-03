num = 5
factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print("Factorial of the num of = " , factorial)    

for i in range(1 , num+1):
    factorial *= i
print("Factorial of the num of = " , factorial)    
