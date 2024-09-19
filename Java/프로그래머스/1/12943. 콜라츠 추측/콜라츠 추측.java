class Solution {
    public int solution(long num) {
        /*
        1. 1이 될 때까지 
        2. 짝수 : 2로 나누기 , count++
        3. 홀수 : 3을 곱하고 1을 더하기 , count++
        4. num이 1이면 0을 리턴 
        5. count가 500번 될 때까지 1이 되지 않으면 -1을 리턴
        */
        int count = 0; 
        
        while(num > 1){
            if(num % 2 == 0){
                num = num / 2;
            }
            else{
                num = (num * 3) + 1; 
            }  
            count++;
            
            if(count > 500){
                return -1;
            }
        }
        
        return count;
    }
}