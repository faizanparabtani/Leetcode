class Problem5 {
    public static String longestPalindrome(String s) {
        int n = s.length();
        int longestP = 1;
        int final_R = 0, final_L = 0;

        for (int i = 0; i < n; i++){
            int L = i, R = i;
            int current_longest = 0;

            while (L >= 0 && R < n){
                if (s.charAt(L) == s.charAt(R)){
                    current_longest += 1;
                    L--;
                    R++;
                }
                else{
                    break;
                }
            }
            if (longestP < current_longest){
                longestP = current_longest;
                final_R = R;
                final_L = L;
            }
        }
        return s.substring(final_L+1, final_R);
    }

    public static void main(String[] args){
        String mystring = "asdmaba";
        String answer = longestPalindrome(mystring);
        System.out.println(answer);
    }
}