class Solution {
    public void sortColors(int[] nums) {
        int zeros = 0;
        int ones = 0;
        int twos = 0;
        for (int i = 0; i< nums.length; i++){
            if (nums[i] == 1){
           nums[twos++] = 2;
           nums[ones++] = 1;
            }
            else if (nums[i] == 2){
            nums[twos++] = 2;

            }
            else{
            nums[twos++] = 2;
            nums[ones++] = 1;
            nums[zeros++] = 0;
            }
        }

       
    }
}