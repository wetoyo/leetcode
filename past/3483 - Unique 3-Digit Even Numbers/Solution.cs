// LeetCode #3483 - Unique 3-Digit Even Numbers
// https://leetcode.com/problems/unique-3-digit-even-numbers/
//
// Difficulty: Easy
// Topics: Array, Hash Table, Recursion, Enumeration
//
// Approach:
//
// Time:  O()
// Space: O()

public class Solution {
    public Dictionary<int,int> dict = new Dictionary<int,int>();
    public int TotalNumbers(int[] digits) {
        TotalNumberHelper(digits, 0, new bool[digits.Length]);
        return dict.Count;

    }

    public void TotalNumberHelper(int[] digits, int num, bool[] used)
    {
        if (num > 99)
        {
            if (num%2 ==0) dict.TryAdd(num, 0);
            return;
        }
        for (int i = 0; i< digits.Length; i++)
        {
            if (used[i] == true) continue;
            if (num == 0 && digits[i] == 0) continue;

            used[i] = true;
            TotalNumberHelper(digits, num * 10 + digits[i], used);
            used[i] = false;
        }
    }
}