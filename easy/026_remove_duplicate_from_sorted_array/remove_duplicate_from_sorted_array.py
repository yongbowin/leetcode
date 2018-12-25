class Solution:
    """
    使用两根指针(下标)，一个指针(下标)遍历数组，另一个指针(下标)只取不重复的数置于原数组中
    """

    # 方法一
    def removeDuplicates_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        
        len_nums = 1
        for i in range(len(nums)-1):
            if nums[i+1] != nums[i]:
                nums[len_nums] = nums[i+1]
                len_nums += 1
            else:
                continue
            
        return len_nums
    
    # 方法二
    def removeDuplicates_2(self, nums):
        if not nums:
            return 0

        newTail = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]

        return newTail + 1

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates_1([1,1,2]))
    print(s.removeDuplicates_2([1,1,2]))
