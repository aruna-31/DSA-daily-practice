class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[mid] == target:
                return True
            if nums[low] == nums[mid] and nums[mid] == nums[high]:
                low = low+1
                high = high-1
                continue
            if nums[low] <=nums[mid]:
                if nums[low] <=target and nums[mid] >=target:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] <=target and nums[high] >=target:
                    low = mid+1
                else:
                    high = mid-1
        return False

        
        