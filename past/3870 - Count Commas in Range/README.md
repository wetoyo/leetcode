# Count Commas in Range

[LeetCode #3870](https://leetcode.com/problems/count-commas-in-range/) — Difficulty: Easy

## Problem
For num n, return num of commas used in all numbers from [1,n]
Ex 1002 - > 3\
1,002 +1\
1,001  +1\
1,000 +1\
999... has no commas\
\_\_\_\_\_\_\_\
 3
## Approach
I went recursively, but I realize in post the implementation is poor. not only is the calculation on each level needlessly expensive, the problem limits the scope to 10e5, so a oneliner of max(0, n-999) would work as well.

## Complexity
- Time: O(logn)
- Space: O(logn)
