# simple generator function

def simple_genertor():
    yield 11
    yield 22
    yield 33
    
print("value iterator in simple_generator: ")
for value in simple_genertor():
    print(value)
    
print("type of simple generator :", type(simple_genertor))



# by using next


def generator_obj():
    yield 11
    yield 22
    yield 33

obj = generator_obj()
print("using next : ")
print(next(obj))
print(next(obj))
print(next(obj))

print("type of generator_obj : ", type(generator_obj))
print("type of obj : ", type(obj))



print(dir(list))


original_list = [1, 1, 1, 2, 3, 3, 4, 4, 4, 4, 5, 6, 6, 7, 7, 7]


unique_list = original_list.count(4)
print(unique_list)



original_list = [1, 1, 1, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 7]

# uniquifying
unique_list = list(dict.fromkeys(original_list))
print(unique_list)


for i in range(100,201):
    if i%2 == 0:
        print(i, end= " ")
    
    
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1.sort(reverse = True)
print(list1)


setA = [10,20,30]
setB = [15,25,35]
product = [(i,j) for i in setA for j in setB]
print(product)