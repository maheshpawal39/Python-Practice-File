n = int(input("Enter Value of N : "))
sum_even = 0

for i in range (1, n+1):
    if i % 2 == 0 :
        sum_even += 1

print("Sum of given even no. is : " , sum_even)        