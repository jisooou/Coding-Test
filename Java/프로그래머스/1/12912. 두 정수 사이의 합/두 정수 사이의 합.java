class Solution {
    public long solution(int a, int b) {
        //int sum > 결괏값X
        long sum = 0;
        
        if(a < b){
            for(int i = a; i < b+1; i++){
                sum = sum + i;
            }
            return sum;
        }
        else if(a > b){
            for(int i = b; i < a+1; i++){
                sum = sum + i; 
            }
            return sum;
        }
        else if(a == b){
            return a; 
        }
        
        
        return sum;
    }
}