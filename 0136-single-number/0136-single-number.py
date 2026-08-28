class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        single = 0
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0)+1
        for i in range(len(nums)):
            
            if freq[nums[i]] == 1:
                return nums[i]

        
        
        