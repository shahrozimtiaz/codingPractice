public class MissingNum {
    public static void main(String[] args){
        int[] arr = new int[100];
        int sum1 =0;
        int sum2 =0;

        for(int i=1;i<=100;i++){
            arr[i-1]=i;
        }
        for(int i=1;i<=100;i++){
            sum1+=i;
        }
        arr[56]=0;
        for(int i=0;i<100;i++){
            sum2+=arr[i];
        }
        System.out.println(sum1-sum2);
    }
}
