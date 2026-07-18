class Solution {
    public int missingNumber(int[] nums) {
        Set<Integer> nums_set = new HashSet<>();
        for (int num : nums){
            nums_set.add(num);
        }
        for (int i = 0; i <= nums.length; i++){
            if (!nums_set.contains(i)){
                return i;
            }
        }
        return -1;
    }
}
