import java.util.Arrays;
import java.util.HashMap;

public class twoSum{
    public static void main(String[] args) {
        int[] test = {3,5,7,11,13,17};

        System.out.println(Arrays.toString(toSum(test,18)));
    }
    
    private static int[] toSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if(map.containsKey(target-num)){
                int[] answer = {map.get(target-num),i};
                return answer;
            }else{
                map.put(num, i);
            }
        }
        return null;
    }
}