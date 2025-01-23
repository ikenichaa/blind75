from typing import List

class Solution:
    def indices(lst, item):
        return [i for i, x in enumerate(lst) if x == item]
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## Use enumerate to get the index
        for i, n in enumerate(nums):
            difference = target - n
            ind_difference = [i for i, x in enumerate(nums) if x == difference]
            ans = list(set([i]) | set(ind_difference))
            if len(ans) == 2:
                return ans




if __name__ == "__main__":
    print(Solution.twoSum(Solution, [1,3,4,2], 6))