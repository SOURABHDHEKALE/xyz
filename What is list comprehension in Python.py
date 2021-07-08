
# What is list comprehension in Python?

squre_no = [i ** 2 for i in range(1,11)]
print(squre_no)



# next


squre_no = [i **2 for i in range(1,11) if i%2 ==0]
print(squre_no)

# next

squre_no = [i ** 2 for i in range(1,11) if i%2 != 0]
print(squre_no)
