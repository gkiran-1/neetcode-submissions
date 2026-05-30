class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_nums = len(nums)
        if len_nums > 1:
            if len_nums == len(set(nums)):
                return False
            else:
                return True
        else:
            return False
        

         