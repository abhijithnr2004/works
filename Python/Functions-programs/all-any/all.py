lst = [10,3,30,24,2,17]

num_gt_five = [n>5 for n in lst]

is_all_gt_five = all(num_gt_five)

print(is_all_gt_five)