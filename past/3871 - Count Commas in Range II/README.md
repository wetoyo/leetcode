# Count Commas in Range II

[LeetCode #3871](https://leetcode.com/problems/count-commas-in-range-ii/) — Difficulty: Medium

## Problem
Same as yesterday, but with 1<=n<=10e15

## Approach
Same as yesterdays, tho i realized yesterdays had some issues. Also, running into a rounding error with Math.Log10 on 999999999999999. Switched to using a loop instead of the log function. 

## Complexity
- Time: O(logn)
- Space: O(logn)
