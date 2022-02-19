class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        self.permutationHelper(nums, [], permutations)
        return permutations
    
    def permutationHelper(self, array, currentPermutations, permutations):
        if not len(array) and len(currentPermutations):
            permutations.append(currentPermutations)
        
        else:
            for i in range(len(array)):
                newArray = array[:i] + array[i+1:]
                newPermutations= currentPermutations + [array[i]]
                self.permutationHelper(newArray, newPermutations, permutations)