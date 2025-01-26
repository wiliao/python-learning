def list_count_4(nums):
  count = 0  
  for num in nums:
    if num == 4: # can be any number
      count = count + 1

  return count
#chanaglable down there
print(list_count_4([1, 4, 6, 7, 4]))
print(list_count_4([1, 4, 6, 4, 7, 4]))