import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class Anagrams {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter two strings to be checked.");
        String str1 = scan.nextLine();
        String str2 = scan.nextLine();
        System.out.println(anagramChecker1(str1,str2));
//        System.out.println(anagramChecker2(str1,str2));
    }
    private static boolean anagramChecker1(String str1, String str2){
        HashMap mp = new HashMap();

        for(char c : str1.toCharArray()){
            if(mp.containsKey(c)){
                mp.put(c,(int) mp.get(c)+1);
            }else{
                mp.put(c,1);
            }
        }
        for(char c : str2.toCharArray()){
            if(mp.containsKey(c)){
                mp.put(c, (int) mp.get(c)-1);
            }else{
                return false;
            }
        }
        for(Object c : mp.keySet()){
            if((int)mp.get(c)!=0) {
               return false;
            }
        }
       return true;
    }
    private static boolean anagramChecker2(String str1, String str2){
       char[] arr1 = str1.toCharArray();
       char[] arr2 = str2.toCharArray();
       Arrays.sort(arr1);
       Arrays.sort(arr2);
       if(!Arrays.equals(arr1,arr2)) {return false;}
       return true;
    }
}