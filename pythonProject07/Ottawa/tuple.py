my_tuple = ("Python","Java","Selenium",987654)
my_tuple1 = (654,432,65432.0,65432)
#datatype
print(type(my_tuple))
#lenght
print(len(my_tuple))
#idexing
print(my_tuple[::-1])
print(my_tuple[::])
print(my_tuple[-1])
print(my_tuple[2:])
add_tuple = my_tuple + my_tuple1
print(add_tuple)
#loop
for i in my_tuple:
    print(i)