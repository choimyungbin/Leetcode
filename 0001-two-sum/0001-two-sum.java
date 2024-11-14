import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hashMap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            if (hashMap.containsKey(complement)) {
                return new int[] { i, hashMap.get(complement) };
            }
            
            hashMap.put(nums[i], i);
        }
        
        throw new IllegalArgumentException("No two sum solution");
    }
}
