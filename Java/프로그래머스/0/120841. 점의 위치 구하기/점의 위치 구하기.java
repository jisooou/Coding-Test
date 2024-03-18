class Solution {
    public int solution(int[] dot) {
        int answer = 0;
        
        if(dot[0] > 0 && dot[1] > 0){
            answer = 1;
            //return answer; -> return을 사용하려면 이와 같이 사용하기.
        }
        else if(dot[0] < 0 && dot[1] > 0){
            answer = 2; 
        }
        else if(dot[0] < 0 && dot[1] < 0){
            answer = 3;
        }
        else if(dot[0] > 0 && dot[1] < 0){
            answer = 4; 
        }
        
        return answer;
    }
}