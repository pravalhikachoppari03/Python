list1 = [1,2,3,4,5]
list2 = [3,5,6,2,7,8]
missing_values = set(list2).difference(list1)
print("Missing values in list1: ",missing_values)
additional_values = set(list1).difference(list2)
print("Additional values in list1: ",additional_values)
missing_values = set(list1).difference(list2)
print("Missing values in list2: ",missing_values)
additional_values = set(list2).difference(list1)
print("Additional  values in list2: ",additional_values)
