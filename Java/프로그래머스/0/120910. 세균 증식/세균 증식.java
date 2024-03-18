class Solution {
    public int solution(int n, int t) {
        int answer = n; //세균 수
        
        for(int i = 0; i < t; i++){ //i는 0부터 t까지. 혹은 1부터 t-1까지 돈다. 
            answer = answer * 2; //세균 수는 계속 2배만큼 증가
        }
        
        return answer;
    }
}
