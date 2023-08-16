class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        [-2, 1,-3, 4, -1, 2, 1 , -5, 4]
         -2,-1,-4, 0  -1  1  2   -3  1
         
         0  -2  1 -2  4   3  5   6   1
         
        -2   0  0  1  1   4  4   5   6
     
        '''
        maxSubSum = nums[0]
        currSum=0
        
        for n in nums:

            if currSum<0:
                currSum=0
            currSum+=n
            maxSubSum = max(maxSubSum,currSum)


        
        return maxSubSum