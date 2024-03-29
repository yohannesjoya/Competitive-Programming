class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        unique = x^y
        while unique !=0:
            count+=1
            unique &= unique-1
        
        return count