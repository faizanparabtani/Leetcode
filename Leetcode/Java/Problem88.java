class Problem88 {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {

        // Merge nums2 into nums1 starting from the end
        int i = m - 1;  // Last valid element in nums1
        int j = n - 1;  // Last element in nums2
        int k = m + n - 1; // Last index of nums1
        
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }
        
        // Copy any remaining elements from nums2
        while (j >= 0) {
            nums1[k--] = nums2[j--];
        }
    }


    public static void main(String[] args){
        int m = 3, n = 3;
        int[] nums1 = {1, 2, 3, 0, 0, 0}; // First array with extra space
        int[] nums2 = {2, 5, 6}; // Second array

        merge(nums1, m, nums2, n);

        for(int i=0; i<nums1.length; i++){
            System.out.println(nums1[i]);
        }

    }
}