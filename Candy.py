# Time Complexity : O(n) 
# Space Complexity :O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Your code here along with comments explaining your approach
class Solution:
    def candy(self, ratings):
        if len(ratings) < 1:
            return 0 
        
        nums = [1 for _ in range(len(ratings))]

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1] + 1 
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                nums[i] = max(nums[i], nums[i]+nums[i+1])
        print(nums)
        candies = 0 
        for candy in nums:
            candies += candy 
        
        return candies
        
if __name__ == "__main__":
    s = Solution()
    print(s.candy([1,0,2]))