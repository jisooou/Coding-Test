class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        
        for(int i = 0; i < n; i++){
            //answer[0] = 2 * (0+1)
            //answer[1] = 2 * (1+1)
            answer[i] = (long) x * (i+1); 
        }
        
        return answer;
    }
}