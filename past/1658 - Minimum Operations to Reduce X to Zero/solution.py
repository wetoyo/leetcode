"""
LeetCode #1658 - Minimum Operations to Reduce X to Zero
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

Difficulty: Medium
Topics: Array, Hash Table, Binary Search, Sliding Window, Prefix Sum

Approach:


Time:  O(n)
Space: O(1)
"""


class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        target = sum(nums) - x
        
        left = 0
        total = 0
        ans = -1
        
        for i in range(len(nums)):
            total += nums[i]
            
            while total > target and left <= i:
                total -= nums[left]
                left += 1
                
            if total == target:
                ans = max(ans, i - left + 1)
                
        return len(nums) - ans if ans != -1 else -1


if __name__ == "__main__":
    sol = Solution()
    # quick manual test(s) here
