class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dit ={}
        for i, ch in enumerate(nums):
            rest = target-ch
            if rest in dit:
                return [dit[rest],i]
            else:
                dit[ch]=i
        return None