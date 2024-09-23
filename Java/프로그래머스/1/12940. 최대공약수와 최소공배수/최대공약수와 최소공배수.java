// for문을 통해 확인
class Solution {
    public int[] solution(int n, int m) {
        
        int[] answer = new int[2];
        int max = 0; 
        
        for(int i = 1; i <= n && i <= m; i++){
            if(n % i == 0 && m % i == 0){
                max = i; 
            }
        }
        answer[0] = max; //max
        answer[1] = (n * m) / max; //min
        
        
        return answer;
    }
}