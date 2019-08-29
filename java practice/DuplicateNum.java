import java.util.LinkedHashMap;

public class DuplicateNum {
    public static void main(String[] args){
        int[] arr = {2,3,3,1,6,4,5};
//        HashMap mp = new HashMap(arr.length);
        LinkedHashMap mp = new LinkedHashMap();
        for(int i=0;i<arr.length;i++){
            if(!mp.containsKey(arr[i])){
                mp.put(arr[i],1);
            }
        }
        for(Object i : mp.keySet()){
            System.out.print(i + " ");
        }
    }
}
