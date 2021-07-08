
# 
# class student:
#     def __init__(self,name,parcentage):
#         self.name = name
#         self.parcentage = parcentage
#         
#     def show(self):
#         print("name is:", self.name, "and parcentage is:", self.parcentage)
# stud = student("jessa",80)       
# stud.show()
#         
#         
#         
# # Python program to illustrate
# #Picle.dumps()
# import pickle
# 
# data = [ { 'a':'A', 'b':2, 'c':3.0 } ]
# data_string = pickle.dumps(data)
# print ('PICKLE:', data_string )
        
        
        
import pickle

# Python object
my_list = [11, 'Python', b'Love Python']

# Pickling
with open("data.pickle","wb") as file_handle:
    pickle.dump(my_list, file_handle, pickle.HIGHEST_PROTOCOL)

print("Pickling completed!")       
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
