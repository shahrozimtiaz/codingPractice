import java.util.ArrayList;

public class HouseRobber {
    public static void main(String[] args) {
        ArrayList<int[]> inputs = new ArrayList<>();
        int[] input1 = {1,2,3,1};
        int[] input2 = {2,7,9,3,1};
        int[] input3 = {5,1,1,5};
        inputs.add(input1);
        inputs.add(input2);
        inputs.add(input3);
        for(int[] input : inputs) {
            System.out.println("rob1: " + rob1(input, 0));
            System.out.println("rob2: " + rob2(input));
            System.out.println("rob3: " + rob3(input));
            System.out.println("-----");
        }
    }
    private static int rob1(int[] input, int i){
        if(i>=input.length){return 0;}

        int curr = input[i];

        int max1 = curr + rob1(input,i+2);

        int max2 =  rob1(input,i+1);

        return Math.max(max1,max2);
    }
    private static int rob2(int[] input){
        int[] dp = new int[input.length];
        dp[0]=input[0];
        dp[1]=Math.max(input[0],input[1]);

        for(int i=2;i<input.length;i++){
            dp[i] = Math.max(dp[i-1],dp[i-2]+input[i]);
        }
        return dp[input.length-1];
    }
    private static int rob3(int[] input){
        int prev2=0;
        int prev=0;

        for(int i=0;i<input.length;i++){
            int current = Math.max(prev,prev2+input[i]);
            prev2=prev;
            prev=current;
        }
        return prev;
    }
}
