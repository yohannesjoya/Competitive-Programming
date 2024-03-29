class Solution {
    public int longestOnes(int[] nums, int k) {
        
        int Zro = 0, i=0;
        int ans = 0;
            
        for (int j=0;j<nums.length;j++){
            
            if (nums[j]==0) Zro++;
                
            while (Zro>k){
                if (nums[i]==0) Zro--;
                i++;
            }
            
            ans = Math.max(ans,j-i+1);
        }
        
        return ans;
        
    }
}