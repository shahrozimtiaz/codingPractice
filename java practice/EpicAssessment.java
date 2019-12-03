import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.lang.Math;
import java.util.Iterator;

public class EpicAssessment {

    static int jumps(int[][] board,int player, int row, int col){
        int path1 = 0;
        int path2 = 0;
        int path3 = 0;
        int path4 = 0;

        if(row>=board.length || col>=board.length){ //out of bounds
            return 0;
        }
        //jump left
        if(col>1){
            if(board[row][col-1] != player && board[row][col-1] != 0 && board[row][col-2]==0){ //can jump
                path1 += 1 + jumps(copyBoard(board,player,row,col-2),player,row,col-2);
            }
        }
        //jump up
        if(row>1){
            if(board[row-1][col] != player  && board[row-1][col] != 0  && board[row-2][col]==0){ //can jump
                path2 += 1 + jumps(copyBoard(board,player,row-2,col),player,row-2,col);
            }
        }

        //jump right
        if(col<board.length-2){
            if(board[row][col+1] != player  && board[row][col+1] != 0  && board[row][col+2]==0){ //can jump
                path3 += 1 + jumps(copyBoard(board,player,row,col+2),player,row,col+2);
            }
        }
        //jump down
        if(row<board.length-2){
            if(board[row+1][col] != player  && board[row+1][col] != 0  && board[row+2][col]==0){ //can jump
                path4 += 1 + jumps(copyBoard(board,player,row+2,col),player,row+2,col);
            }
        }
        return Math.max(Math.max(path1,path2),Math.max(path3,path4));
    }

    static int[][] copyBoard(int[][] board, int player, int row, int col){ //helper function for copying the state of the current board then updating new player location
        int n = board.length;
        int[][] copyBoard = new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                copyBoard[i][j] = board[i][j];
            }
        }
        copyBoard[row][col]=player;
        return copyBoard;
    }

    static void passwords(int n){
        if(n<0){
            System.out.println("Invalid n");
        }else{
            String upperAlph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
            String lowerAlph = "abcdefghijklmnopqrstuvwxyz";
            recur(n,0,upperAlph,lowerAlph,"");
            recur2(n,0,upperAlph,lowerAlph,"");
        }
    }

    static void recur(int n, int i,String upperAlph, String lowerAlph, String curr){
        if(curr.length()>n){
            return;
        }
        if(i>=lowerAlph.length()){
            return;
        }
        if(curr.length()==n){
            System.out.println(curr);
        }
        recur(n,i+1,upperAlph,lowerAlph,curr); //dont include lowerCase
        recur(n,i+1,upperAlph,lowerAlph,curr+=lowerAlph.charAt(i)); //include lowerCase
        recur(n,i+1,upperAlph,lowerAlph,curr); //dont include upperCase
        recur(n,i+1,upperAlph,lowerAlph,curr+=upperAlph.charAt(i)); //include upperCase
    }

    static void recur2(int n, int i,String upperAlph, String lowerAlph, String curr){
        if(curr.length()>n){
            return;
        }
        if(i>lowerAlph.length()){
            return;
        }
        if(curr.length()==n){
            System.out.println(curr);
        }
        recur(n,i+1,upperAlph,lowerAlph,curr); //dont include upperCase
        recur(n,i+1,upperAlph,lowerAlph,curr+=upperAlph.charAt(i)); //include upperCase
        recur(n,i+1,upperAlph,lowerAlph,curr); //dont include lowerCase
        recur(n,i+1,upperAlph,lowerAlph,curr+=lowerAlph.charAt(i)); //include lowerCase
    }

    static String convert(int n, String str){
        int ogN = n;
        String vowels = "aeiou";
        String consonants = "bcdfghjklmnpqrstvwxyz";
        StringBuilder results = new StringBuilder();

        for(char ch : str.toCharArray()){
            n = ogN;
            if(vowels.contains(String.valueOf(ch))){
                int i = vowels.indexOf(ch);
                while(n>0){
                    n--;
                    i++;
                    if(i>vowels.length()){
                        i = 0;
                    }
                }
                results.append(vowels.charAt(i));
            }else{
                n = n * n;
                int i = consonants.indexOf(ch);
                while(n>0){
                    n--;
                    i++;
                    if(i>consonants.length()){
                        i = 0;
                    }
                }
                results.append(consonants.charAt(i));
            }

        }
        return results.toString();
    }

    static void finder(String str){ //check
        HashSet<String> set = new HashSet<String>();
        if(str == null){
            System.out.println("Entered a null string");
        }else{
            for(int len = 3; len <= str.length(); len++){
                for(int i = 0;i + len-1 < str.length();i++){
                    String toCheck = str.substring(i,i+len);
                    if(isPalinDrome(toCheck)){
                        set.add(toCheck);
                    }
                }
            }
        }
        Iterator<String> i = set.iterator();
        while (i.hasNext())
            System.out.println(i.next());
    }

    static boolean isPalinDrome(String str){ //helper function to check if str is a palinDrome
        int s = 0;
        int e = str.length()-1;
        while(s<=e){
            if(str.charAt(s) != str.charAt(e)){
                return false;
            }
            s++;
            e--;
        }
        return true;
    }

    public static void main(String[] args) {
        int[][] board = new int[4][4];
        board[0][1] = 1;
        board[0][2] = 2;
        board[1][0] = 0;
        board[1][1] = 1;
        board[1][2] = 2;
        board[2][1] = 1;
        board[2][2] = 1;
        board[2][3] = 0;
        board[3][2] = 0;
        board[3][1] = 1;
        board[3][3] = 2;
        for(int[] arr: board)
            System.out.println(Arrays.toString(arr));

        System.out.println(jumps(board,2,1,2));
    }
}
