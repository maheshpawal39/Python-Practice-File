def sum_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)
print(sum_all(1,2,3))
# print(sum_all(12,23,34,45,56))
# print(sum_all(11,22,33,44,55))