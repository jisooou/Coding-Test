class Solution {
    public int solution(int n) {
        /* 
        1. 1~n까지 돈다. 
        2. 1씩 증가하는 숫자의 합이 15와 같을 때 count (i도 1씩 증가)
        3. count의 합을 리턴
        */
        
        int count = 0; 
        
        for(int i = 1; i <= n; i++){
            int sum = 0; 
            
            for(int j = i; j <= n; j++){
                sum = sum + j; 
                
                if(sum == n){
                    count++;
                    break;
                }
                
                if(sum > n){
                    break;
                }
                
            }
        }
        
        return count;
    }
}