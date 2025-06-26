class Problem605 {
    // public static boolean canPlaceFlowers(int[] flowerbed, int n) {
    // 	int flowerbedLength = flowerbed.length;
    // 	int L, R;

    // 	// Checking if no flower needs to be planted
    // 	if (n == 0){
    // 		return true;
    // 	}

    // 	for (int i=1; i+1 < flowerbedLength; i++){
    // 		L = i - 1;
    // 		R = i + 1;
    // 		System.out.printf("L: %d, R: %d, n: %d\n", L, R, n);
    // 		// First element
    // 		if (L < 0){
	//     		if (flowerbed[i] == 0 && flowerbed[i+1] != 1){
	//     			flowerbed[i] = 1;
	//     			n--;
	//     			continue;
	//     		}
    // 		}

    // 		if (flowerbed[i] == 0 && flowerbed[L] == 0 && flowerbed[R] == 0){
    // 			flowerbed[i] = 1;	
	// 			n--;
    // 		}
    		
    // 	}

    // 	if (flowerbed[flowerbedLength-1] == 0 && flowerbed[flowerbedLength-2] == 0){
	// 		System.out.printf("Second print n: %d\n", n);
    // 		n--;
    // 	}

    // 	return (n <= 0) ? true : false;
    // }

    public static boolean canPlaceFlowers(int[] flowerbed, int n) {
        if (n == 0) return true;
        for (int i = 0; i < flowerbed.length; i ++) {
            if (flowerbed[i] == 0 && (i == 0 || flowerbed[i - 1] == 0) && (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) { // can place?
                -- n;
                if (n == 0) return true;
                flowerbed[i] = 1; // place!
            }
        }
        return false;
    }


    public static void main(String[] args) {
        int[] nums = {1,0,0,0,0,1};
        int n = 2;
        System.out.println(canPlaceFlowers(nums, n));
    }
}

// Case 1 n-1
// 1,0,0,0,1	


// 1,0,0,1,0,1
