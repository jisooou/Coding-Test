class Solution {
    public String solution(int n) {
        /*
        1. 1만큼 돌을 때, "수" 리턴
        2. n만큼 돌리면 n만큼 "수", "박"을 리턴
        */
        String answer = "";
      
        for(int i = 0; i < n; i+=2){
            answer += "수";
            for(int j = i+1; j < n; j+=2){
                answer += "박";
                break;
            }
        }
     
        return answer;
    }
}