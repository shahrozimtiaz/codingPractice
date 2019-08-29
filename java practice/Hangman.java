import java.io.File;
import java.util.HashMap;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class Hangman {
    static Scanner input;
    static StringBuilder current;
    static int attempts = 11;
    static String[] possLetters = {"","ai","aoeimhnustyblpxdfrwgjk","aeoitsuprndbgmylhwfckxvjzq","aesoirltnudpmhcbkgywfvjzxq","searoiltnudcypmhcbkgwfvjzxq","esariolntducmpghbykfwvzxjq","esiarntolducgpmhbyfkwvzxjq","esiarntoldcugmphbyfkwvzxqj","esirantolcdugmphbyfvkwzxqj","eisrantolcdugmphbyfvkwzxqj","eisnartolcudpmghbyfvkwzxqj","eisntarolcpumdghybvfzkwxqj","ientsaorlcpumgdhybvfzxkwqj","ietsnaorlcpumdhgybvfzxkwqj","ietnsoarlcpumdhgybvfzxwkqj","ietsnaorlcpumhdygbvfzxwqkj","ietnsoarlcpumhdgybvfzxqwjk","isetonralcpmuhdgybvzfxqwk","ietonasrlcpmuhdgybvfzxkjqw","ioetrsanclphumydgbzvfkxjq"};
    static String commonUncommon = "ywf";
    static int noNum = 0;
    static HashMap<String,Integer> originalDictionary;
    public static void main(String[] args) {
        HashMap<String,Integer> dictionary = new HashMap<>();
        try{
             Scanner file = new Scanner(new File("words.txt"));
             while(file.hasNextLine()){
                 dictionary.put(file.nextLine().toLowerCase(),1);
            }
        } catch (Exception e){
            e.printStackTrace();
        }
        originalDictionary = (HashMap) dictionary.clone();
        game(dictionary);
    }
    public static void game(HashMap dictionary){
//        String letters = "etaoinshrdlubcfgyzjkmpqvwx";
//        String other = "bcfgyzjkmpqvwx";
        input = new Scanner(System.in);
        System.out.println("Hello traveller, welcome to hangman. I will have "  + attempts + " guesses to guess your word. What is the length of your word?");
        int length = input.nextInt();
        input.nextLine();
        String letters = possLetters[length];
        HashMap<String,Integer> tempDict = new HashMap<>();
        for(Object o : dictionary.keySet()){
            String word = String.valueOf(o);
            if(word.length()==length){
                tempDict.put(word,1);
            }
        }
        dictionary = (HashMap) tempDict.clone();
        current = new StringBuilder();
        for(int i=0;i<length;i++){
            current.append('-');
        }
        System.out.println("Okay. Let us begin.");
        String[] locations;
        for(int li=0;li<letters.length();li++) {
            char l = letters.charAt(li);
            if(l!='-') {
                if (attempts < 1) {
                    break;
                }
                if (current.indexOf("-") == -1) {
                    System.out.println("Your word is '" + current + "'.");
                    System.out.println("Better Luck next time.");
                    System.exit(0);
                }
                if(noNum==3){
                    noNum=0;
                    boolean ava = false;
                    for(char c : commonUncommon.toCharArray()){
                        if(c!='-'){
                            ava = true;
                            break;
                        }
                    }
                    if(ava) {
                        li--;
                        int rand;
                        do {
                            rand = ThreadLocalRandom.current().nextInt(0, commonUncommon.length());
                        } while (commonUncommon.charAt(rand) == '-');
                        l = commonUncommon.charAt(rand);
                    }
                }
                letters = letters.replace(l,'-');
                commonUncommon = commonUncommon.replace(l,'-');
                boolean available = false;
                boolean breakOutter = false;
                for (Object o : dictionary.keySet()) {
                    String check = String.valueOf(o);
                    for (char c : check.toCharArray()) {
                        if (c == l) {
                            available = true;
                            breakOutter = true;
                            break;
                        }
                    }
                    if (breakOutter) {
                        break;
                    }
                }
                if (available) {
                    System.out.println(current);
                    String temp = ask(l);
                    if (temp != null) {
                        locations = temp.split(",");
                        for (String strNum : locations) {
                            int loc = Integer.valueOf(strNum);
                            current.replace(loc - 1, loc, String.valueOf(l));
                        }
                        for (int ind = 0; ind < current.length(); ind++) {
                            tempDict = new HashMap<>();
                            if (current.charAt(ind) != '-') {
                                for (Object o : dictionary.keySet()) {
                                    String maybe = String.valueOf(o);
                                    if (maybe.charAt(ind) == current.charAt(ind)) {
                                        tempDict.put(maybe, 1);
                                    }
                                }
                                dictionary = (HashMap) tempDict.clone();
                            }
                        }
                    }
                }
            }
        }
        if(dicitionaryCheck()) {
            System.out.println("oh, you are worthy. Well played.");
        }
    }
    public static void attempts(){
        System.out.println("I have " + attempts + " attempts left.");
    }
    public static String ask(char l){
        attempts();
        System.out.println("Does your word have 1 or more '" + l + "'? (Enter y or n)");
        while(true) {
            String response = input.nextLine();
            if (response.equals("y")) {
                noNum=0;
                int counter = 0;
                for(int i=0;i<current.length();i++){
                    if(current.charAt(i) == '-'){
                        counter++;
                    }
                }
                if(counter>1) {
                    System.out.println("Enter the location(s) of the letters. I.e. 1,3 or 1,2 or 12,5 or 5 etc.");
                    return input.nextLine();
                }else{
                    current.replace(current.indexOf("-"),current.indexOf("-")+1 ,l + "");
                    return null;
                }
            } else if (response.equals("n")) {
                attempts--;
                noNum++;
                return null;
            } else{
                System.out.println("Invalid input. Try again.");
            }
        }
    }
    static boolean dicitionaryCheck(){
        System.out.println("What's the word, let me check if it's in my dictionary.");
        String dicCheck = input.nextLine();
        System.out.println("The word is in my dictionary: " + originalDictionary.containsKey(dicCheck));
        return originalDictionary.containsKey(dicCheck);
    }
}