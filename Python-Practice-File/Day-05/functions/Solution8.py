def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key } : {value}")


print_kwargs(name = "Shaktiman" , power = "laizer")   
print_kwargs(name = "Shaktiman" )   
print_kwargs(name = "Shaktiman" , power = "laizer" , Enmmy = "Dr. Jackal")   