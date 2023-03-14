import java.util.*;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int size = nums.length /2;
        
        HashSet<Integer> set = new HashSet<>();
        for(int i=0; i<nums.length; i++){
            set.add(nums[i]);
        }
        System.out.println(set);
        if (size > set.size()){
            answer = set.size();
        }else{
            answer = size;
        }
        return answer;
    }
}
