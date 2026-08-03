item = ['apple' , 'banana' , 'lichi' , 'lichi' , 'orange' , 'apple' , 'mango']

unique_item = set()

for i in item:
    if i in unique_item:
        print("Duplicates : " , i)
        break
    unique_item.add(i)
