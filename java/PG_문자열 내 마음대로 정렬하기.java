import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        String[] answer = {};
        ArrayList<String> list = new ArrayList<String>();
        
        for(int i=0;i<strings.length;i++){
            list.add(strings[i].charAt(n)+strings[i]);           
        }
        
        answer = list.toArray(new String[list.size()]);
        Arrays.sort(answer);
        
        for(int i=0;i<answer.length;i++){
           answer[i] =  answer[i].substring(1);
        }
        return answer;
    }
}