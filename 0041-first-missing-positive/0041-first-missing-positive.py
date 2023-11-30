class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
             
            while i != nums[i]-1 and 0<nums[i] <=n and nums[i] != nums[nums[i]-1]:
                
                temp = nums[nums[i]-1]
                nums[nums[i]-1] = nums[i]
                nums[i] = temp
                
            
        for i in range(n):
            if nums[i] != i+1 : return i+1
        
        return  n+1
            
     