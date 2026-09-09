// LeetCode #3870 - Count Commas in Range
// https://leetcode.com/problems/count-commas-in-range/
//
// Difficulty: Easy
// Topics: Math
//
// Approach:
//
// Time:  O(logn)
// Space: O(logn)

public class Solution {
    public int CountCommas(int n) {
        return CountCommaHelper(n);
    }
    public int CountCommaHelper(int n){
        if (n < 1000)return 0; 
        int commas = (int)(Math.Log10(n)/3);
        int count = n - (int)Math.Pow(1000, commas) + 1;
        return commas * count + CountCommaHelper((int)Math.Pow(1000, commas)-1);
    }
}
