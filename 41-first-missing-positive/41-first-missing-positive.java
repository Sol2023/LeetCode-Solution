public class Solution {
public int firstMissingPositive(int[] nums) {
    int[] bucket = new int[nums.length + 1];
    for (int n : nums) {
        if (n > 0 && n <= nums.length) bucket[n]++;
    }
    for (int i = 1; i < bucket.length; i++) {
        if (bucket[i] == 0) return i;
    }
    return bucket.length;
    }
}