test_keys = ["sourabh", "rahual", "sonal"]
test_value = [82, 58, 95]
print("original keys list is:" + str(test_keys))
print("original values list is:" + str(test_value))

res = {}
for key in test_keys:
    for value in test_value:
        res[key] = value
        test_value.remove(value)
        break
        
print("resultant dictionary is:" + str(res))


# next method

test_keys = ["sourabh", "rahual", "sonal"]
test_value = [82, 58, 95]
print("original keys list is:" + str(test_keys))
print("original values list is:" + str(test_value))
res = dict(zip(test_keys, test_value))
print("resultant dictionary is:" + str(res))



# next method
# using dictionary comprehension
# to convert lists to dictionary



test_keys = ["sourabh", "rahual", "sonal"]
test_value = [82, 58, 95]
print("original keys list is:" + str(test_keys))
print("original values list is:" + str(test_value))
res = {test_keys[i] : test_value[i] for i in range(len(test_keys))}
print("resultant dictionary is:" + str(res))






