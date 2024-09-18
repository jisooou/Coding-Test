class Solution {
    public int solution(int n) {
        int answer = 0;
        
        for(int x = 1; x < n+1; x++){
            if(n % x == 1){
                answer = x;
                //가장 작은 자연수를 리턴해야 하니까 break.
                break;
            }
        }
        
        return answer;
    }
}