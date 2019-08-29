import java.util.*;

public class EqualsPrac {
    public static void main(String[] args){
        String s1 = "hello";
        String s2 = "hello";
        String s3 = new String("hello");
        System.out.println(checker(s1,s2));
        System.out.println(checker(s1,s3));
    }
    private static boolean checker(String s1,String s2){
       return s1==s2;
    }
}
