class Solution {
    public String solution(String s) {
        String answer = "";
        String [] arr = s.split("");
        
        int middle = arr.length/2;
        if (arr.length%2 == 0){
            answer = arr[middle-1].concat(arr[middle]);
        }else{
            answer = arr[middle];
        }
        return answer;
    }
}