class Problem135 {
    public static int candy(int[] ratings) {
        int ratings_length = ratings.length;
        int[] result_array = int[1] * ratings_length;
        System.out.println(result_array);
    }


    public static void main(String[] args){
        int[] ratings = {1, 0, 2};
        int result = candy(ratings);
        System.out.println(result);
    }
}