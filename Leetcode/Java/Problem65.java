class Problem65 {
    public static int searchInsert(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;

        while (left <= right){
            int middle = left + (right-left) / 2;
            if (nums[middle] == target){
                return middle;
            }else if (nums[middle] > target){
                right = middle - 1;
            }
            else{
            	left = middle + 1;
            }
        }
        return left;
    }

    public static void main(String[] args){
    	int[] nums = {1,3,5,6};
    	int target = 7;

    	int answer = searchInsert(nums, target);
    	System.out.println(answer);
    }
}