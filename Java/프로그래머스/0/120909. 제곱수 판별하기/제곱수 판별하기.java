// 제곱수 구하기 : Math.sqrt()
class Solution {
    public int solution(int n) {
        
        double answer = Math.sqrt(n);
        
        if( answer % 1 == 0 ){
            return 1;
        }
        else{
            return 2; 
        }
        
    }
}