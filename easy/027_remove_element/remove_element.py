class Solution:
    # 第一种方法
    def removeElement_1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 定义两个指针, p1是与val不想等的那些元素的索引，用来覆盖nums
        p1 = 0
        # p2遍历元素
        for p2 in nums:
            if p2 != val:
                nums[p1] = p2 # 覆盖数组nums
                p1 += 1

        return p1

    def removeElement_2(self, nums, val):
        """
        定义两个指针left和right (头指针和尾指针), 充分利用nums的顺序可变的条件(只要nums[left]==val, 就将nums[left]替换掉)
        指针left用来和val比较, 同时,当left所指的元素和val相等时， 指针right用来替换当前元素
        在替换之后, 新元素依然会和val比较
        """
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1 # 只要有相等出现, 该值就会减去1
            else:
                left += 1

        return right

if __name__ == "__main__":
    s = Solution()
    # 测试 nums=[3, 6, 2, 1, 2, 4], val=2
    # 新的数组为nums=[3, 6, 1, 4, 2, 4], 最后两个元素没有被重新赋值
    print(s.removeElement_1([3, 6, 2, 1, 2, 4], 2))
    print(s.removeElement_2([3, 6, 2, 1, 2, 4], 2))
