#Smallest Subarray with a given sum (easy)

#Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

def smallest_subarray_with_given_sum(s, arr):
  # TODO: Write your code here
  if sum(arr) < s:
    return 0
  start = 0
  tempSum = 0
  tempSize = 0
  minSize = -1
  for i in range(len(arr)):
    if tempSum < s:
      tempSum += arr[i]
      tempSize += 1
    while tempSum >= s:
      if minSize != -1:
        minSize = min(minSize, tempSize)
      else:
        minSize = tempSize
      tempSum -= arr[start]
      start += 1
      tempSize -= 1

  return minSize

    
  return -1
