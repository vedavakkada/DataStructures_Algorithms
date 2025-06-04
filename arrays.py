def kadanes(nums):

  currSum = 0
  maxSum = 0

  n = len(nums)

  for i in range(n):

    currSum = max(0, currSum)
    currSum += nums[i]
    maxSum = max(currSum, maxSum)

  return maxSum


# sliding window with constant window
def sliding(nums, k):
    
    seen = set()
    
    L = 0
    n = len(nums)
    for R in range(n):
        
        if R - L + 1 > k:
            seen.remove(nums[L])
            L += 1
        
        if nums[R] in seen:
            return True
            
        seen.add(nums[R])
            
    return False
