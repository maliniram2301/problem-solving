def remove_nums(int_list):
2	  #list starts with 0 index
3	  position = 3 - 1 
4	  idx = 0
5	  len_list = (len(int_list))
6	  while len_list>0:
7	    idx = (position+idx)%len_list
8	    print(int_list.pop(idx))
9	    len_list -= 1
10	nums = [10,20,30,40,50,60,70,80,90]
11	remove_nums(nums)
