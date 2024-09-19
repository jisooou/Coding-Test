//제곱급 > Math.sqrt()
class Solution {
    public long solution(long n) {
        //어떻게 제곱수를 판별할 수 있는지 판단 
        
        long answer = 0;
        long sqrt = (long) Math.sqrt(n);
        
        if(sqrt * sqrt == n){
            answer = (sqrt + 1) * (sqrt + 1);
        }
        else{
            answer = -1;
        }
            
        return answer;
    }
}