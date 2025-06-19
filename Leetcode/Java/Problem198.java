import java.lang.Math;

class Problem198 {
    public static int rob(int[] nums) {
        int nums_length = nums.length;

        if (nums_length == 0 || nums == null){
            return 0;
        }

        if (nums_length == 1){
            return nums[0];
        }

        // [rob1, rob2, i]
        int rob1 = 0; // Represents max profit up to (i-2) houses. Initially set to 0 as i-2 == -1
        int rob2 = nums[0]; // Represents max profit up to (i-1) houses. Initally set to nums[0]
        int temp;

        for(int i=1; i<nums_length; i++){
            temp = Math.max(nums[i]+rob1, rob2);
            rob1 = rob2;
            rob2 = temp; 
            System.out.printf("temp: %d, rob1: %d, rob2: %d%n", temp, rob1, rob2);
        }
        return rob2;
    }

    public static void main(String[] args){
        int[] arr = {1,2,3,1};
        int ans = rob(arr);
        System.out.println(ans);
    }
}