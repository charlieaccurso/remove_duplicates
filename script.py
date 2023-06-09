class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k= None
        if len(nums) == 1:
            k= 1
            return k

        pointer= 1
        while pointer < len(nums):
            if pointer + 1 == len(nums):
                if nums[pointer] == nums[pointer-1]:
                    nums= nums[:pointer]
                    pointer+= 1
                else:
                    pointer+= 1
            else:
                if nums[pointer] == nums[pointer-1]:
                    nums.pop(pointer)
                else:
                    pointer+= 1

        k= len(nums)
        return k
