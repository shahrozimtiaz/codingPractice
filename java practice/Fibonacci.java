import java.math.BigInteger;
import java.util.Scanner;

public class Fibonacci {
    private static BigInteger[] memo;
    public static void main(String[] args){
        while(true) {
            Scanner scan = new Scanner(System.in);
            System.out.println("Enter a number");
            try {
                int n = scan.nextInt();
                memo = new BigInteger[n + 1];
                System.out.println(fib(n));
            } catch (Exception e) {
                e.printStackTrace();
                System.exit(0);
            }
        }
    }
    private static BigInteger fib(int n){
        if(n<=1){return BigInteger.valueOf(n);}
        if (memo[n]!=null){
            return memo[n];
        }
        memo[n]=fib(n-1).add(fib(n-2));
        return memo[n];
    }
}