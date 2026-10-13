"""
LeetCode #3727 - Maximum Alternating Sum of Squares
https://leetcode.com/problems/maximum-alternating-sum-of-squares/

Difficulty: Medium
Topics: Array, Greedy, Sorting

Approach:


Time:  O(nlogn)
Space: O(n)
"""


class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        half = (len(nums)//2)
        arr = [abs(i) for i in nums]
        arr.sort()
        for i in range(half):
            total += arr[i]**2
            total -= arr[i+half]**2
        if (2*half < len(nums)):
            total -= arr[-1]**2
        return -1 * total
        
if __name__ == "__main__":
    sol = Solution()
    # quick manual test(s) here
