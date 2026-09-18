public class Solution
{
    public int FirstStableIndex(int[] nums, int k)
    {
        int n = nums.length; 
        int[] maxn = new int[n];
        int[] minn = new int[n];
        maxn[0] = nums[0];
        for (int i = 1; i < n; i++) {
            maxn[i] = Math.max(maxn[i - 1], nums[i]);
        }
        minn[n - 1] = nums[n - 1];
        for (int i = n -2; i >= 0; i--)
        {
            minn[i]= Math.min(minn[i + 1], nums[i]);
        }
        for (int i = 0; i < n; i++)
        {
            if (maxn[i] <= minn[i] + k)
            {
                return i;
            }
        }
        return -1;

    }
}
