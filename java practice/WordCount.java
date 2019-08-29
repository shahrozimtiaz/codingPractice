import java.util.Scanner;
import java.io.File;

public class WordCount {
    public static void main(String[] args){
        try {
            Scanner input = new Scanner(new File("mobydick.txt"));
            System.out.println(input.nextLine());
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}