class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        if len_nums > 1:
            for i in range(len_nums-1):
                if nums[i] in nums[i+1:]:
                    return True
            return False
        else:
            return False
        

         