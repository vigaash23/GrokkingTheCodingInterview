#Maximum Sum Subarray of Size K (easy)

def max_sub_array_of_size_k(k, arr):
  # TODO: Write your code here
  start = 0
  tempSum = 0
  maxSum = 0
  for i in range(len(arr)):
    tempSum += arr[i]
    if i > k - 1:
      tempSum -= arr[start]
      start += 1
    maxSum = max(tempSum, maxSum)

  return maxSum
