def even_genrator(Limits):
    for i in range(1 , Limits + 1 , 2):
        yield i

for num in even_genrator(10):
    print(num)
