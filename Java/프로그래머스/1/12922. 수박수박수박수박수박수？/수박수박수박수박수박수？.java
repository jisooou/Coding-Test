class Solution {
    public String solution(int n) {
        /*
        1. 인덱스가 짝수 > "수" 리턴
        2. 인덱스가 홀수 > "박" 리턴
        */
        String answer = "";
      
        for(int i = 0; i < n; i++){
            if(i % 2 == 0){
                answer = answer + "수";
            }
            else{
                answer = answer + "박";
            }
        }
     
        return answer;
    }
}