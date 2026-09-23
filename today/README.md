# Minimum Operations to Reduce X to Zero

[LeetCode #1658](https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/) — Difficulty: Medium

## Problem
given a number x, and an array with no negative values, what is the combined length of the shortest prefix and suffix combination that sums to x (they describe the prefix and suffix values subtracting off x but whatever.

## Approach
search instead for the smallest subarray with sum sum(nums) - x

## Complexity
- Time: O(n)
- Space: O(1)
