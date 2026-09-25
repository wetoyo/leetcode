"""
LeetCode #3550 - Smallest Index With Digit Sum Equal to Index
https://leetcode.com/problems/smallest-index-with-digit-sum-equal-to-index/

Difficulty: Easy
Topics: Array, Math

Approach:


Time:  O(n)
Space: O(1)
"""


class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            total = 0
            temp = nums[i]
            while (temp > 0):
                total += temp % 10
                temp /= 10
                if (total > i): break
            if (total == i): return i
        return -1
            

if __name__ == "__main__":
    sol = Solution()
    # quick manual test(s) here
