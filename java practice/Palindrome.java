import java.util.Scanner;

public class Palindrome {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter a string.");
        String str = scan.nextLine();
        System.out.println(palinChecker(str));
    }
    private static boolean palinChecker(String str){
        int i=0;
        int j=str.length()-1;
        while(i<j){
            if(str.charAt(i) != str.charAt(j)){
                return false;
            }
            i++;j--;
        }
        return true;
    }
}
