class Solution {
    public int solution(int[] number) {
        /*
        3개의 값을 찾아야 하니까 for문 3번 돌리기
        */
        int answer = 0;
        
        for(int i = 0; i < number.length; i++){
            for(int j = i+1; j < number.length; j++){
                for(int k = j+1; k < number.length; k++){
                    
                    if(number[i] + number[j] + number[k] == 0){
                        answer++;
                    }
                }
            }
        }
        
        return answer;
    }
}