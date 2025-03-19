class Problem45{
    public static int jump(int[] nums) {
        int minJump = 0;

        for(int i = 0; i < nums.length; i++){
            if(i == nums.length - 1){
                return minJump;
            }
            if(nums[i] == 0){
                return -1;
            }
            int maxJump = 0;
            int maxJumpIndex = 0;
            for(int j = 1; j <= nums[i]; j++){
                if(i + j >= nums.length - 1){
                    return minJump + 1;
                }
                if(i + j + nums[i + j] > maxJump){
                    maxJump = i + j + nums[i + j];
                    maxJumpIndex = i + j;
                }
            }
            i = maxJumpIndex - 1;
            minJump++;
        }
        return minJump;

    }

    public static void main(String[] args) {
        int[] nums = {2,3,1,1,4};
        System.out.println(jump(nums));
    }
}