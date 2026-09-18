# Daily problem - Smallest Stable Index I

[LeetCode #3903](https://leetcode.com/problems/smallest-stable-index-i/description/?envType=daily-question&envId=2026-09-04) — Difficulty: Easy

## Problem
You are given an integer array nums of length n and an integer k.

For each index i, define its instability score as max(nums[0..i]) - min(nums[i..n - 1]).

In other words:

    max(nums[0..i]) is the largest value among the elements from index 0 to index i.
    min(nums[i..n - 1]) is the smallest value among the elements from index i to index n - 1.

An index i is called stable if its instability score is less than or equal to k.

Return the smallest stable index. If no such index exists, return -1.

 

## Approach
Been a while since I did leetcode, this repo is my way of getting back into it. Lucky for me, today is an easy, so I will try to do both python and c#.



## Complexity
- Time: O()
- Space: O()
