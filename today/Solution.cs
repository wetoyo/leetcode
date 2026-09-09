// LeetCode #3871 - Count Commas in Range II
// https://leetcode.com/problems/count-commas-in-range/
//
// Difficulty: Medium
// Topics: Math
//
// Approach:
//
// Time:  O(logn)
// Space: O(logn)

public class Solution {
    public long CountCommas(long n) {
        return CountCommaHelper(n);
    }
    public long CountCommaHelper(long n){
        if (n < 1000)return 0; 
        long commas = 0;
        long temp = n;
        long pwr = 1;
        while (temp >= 1000)
        {
            temp/=1000;
            pwr*=1000;
            commas++;
        }
        long count = n - pwr +1;
        return commas * count + CountCommaHelper(pwr-1);
    }
}
