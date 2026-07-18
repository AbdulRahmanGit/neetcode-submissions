class Solution {
    public int majorityElement(int[] nums) {
        int res=0, max=0;
        HashMap<Integer,Integer> seen = new HashMap<>();
        for (int i = 0;i < nums.length;i++){
            seen.put(nums[i], seen.getOrDefault(nums[i], 0) + 1);
            if (seen.get(nums[i]) > max){
                res = nums[i];
                max = seen.get(nums[i]);
            }
            }
        return res;
    }
}