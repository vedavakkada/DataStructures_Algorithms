def kadanes(nums):

  currSum = 0
  maxSum = 0

  n = len(nums)

  for i in range(n):

    currSum = max(0, currSum)
    currSum += nums[i]
    maxSum = max(currSum, maxSum)

  return maxSum
  
