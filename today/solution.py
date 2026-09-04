class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxn = [0] * len(nums)
        minn = [0] * len(nums)

        maxn[0] = nums[0]

        for i in range(1, len(nums)):
            maxn[i] = max(maxn[i-1], nums[i])

        minn[-1] = nums[-1]

        for i in range(len(nums)-2, -1, -1):
            minn[i] = min(minn[i+1], nums[i])

        for i in range(len(nums)):
            if maxn[i] <= minn[i] + k:
                return i

        return -1

if __name__ == "__main__":
    sol = Solution()
    # quick manual test(s) here
    print(sol.firstStableIndex([1, 6, 2, 4, 5], 3))

# Seems like there should be a better way

# O(n) time, O(n) space solution