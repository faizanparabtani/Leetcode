import java.util.Arrays;

class Problem274 {
    public static int hIndex(int[] citations) {
        int total = 0;
        int n = citations.length;
        int[] temp = new int[n+1];
        Arrays.fill(temp, 0);

        for (int i=0; i<n; i++){
            if (citations[i] > n){
                temp[n] += 1;
            }else{
                temp[citations[i]] += 1;
            }
        }


        for (int i=n; i>-1; i--){
            total += temp[i];
            if (total >= i){
                return i;
            }
        }
        return 0;
    }

    public static void main(String[] args){
        int[] citations = {3,0,6,1,5};
        int answer = hIndex(citations);
        System.out.println(answer);
    }
}