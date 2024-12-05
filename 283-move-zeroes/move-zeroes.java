import java.util.ArrayList;

class Solution {
    public void moveZeroes(int[] nums) {
        int lastIdx = 0;
        int size = nums.length;

        for (int i=0; i<size; i++){
            if (nums[i] != 0){
                nums[lastIdx] = nums[i];
                lastIdx++;
            }
        }

        for (int i=lastIdx; i<size;i++){
            nums[i] = 0;
        }
    }
}