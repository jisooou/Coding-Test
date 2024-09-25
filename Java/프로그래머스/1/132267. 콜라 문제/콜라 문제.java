class Solution {
    public int solution(int a, int b, int n) {
        /* 
            예) 콜라 빈병2개 (a) -> +1병 (b)
            > n/a, n%a
        */
        int answer = 0;
        
        while(n >= a){
            answer += (n/a)*b; 
            n = (n/a)*b + (n%a);     
        }
        
        return answer;
    }
}