class Solution {
    public int[] getConcatenation(int[] nums) {
        int n = nums.length;
        int[] arr = new int[2 * n];
        int idx = 0;
        for(int i = 0; i < 2; i++){
            for (int num: nums){
                arr[idx++] = num;
            }
        }
        return arr;
    }
}