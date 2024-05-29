l1 = [2,4,1,6,7,9]
l2 = [1,3,5,7,8]
diff_l1_l2 = list(set(l1) - set(l2))
diff_l2_l1 = list(set(l2) - set(l1))
total = diff_l1_l2 + diff_l2_l1
print(total)
