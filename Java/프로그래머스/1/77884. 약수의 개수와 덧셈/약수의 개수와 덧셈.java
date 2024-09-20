class Solution {
    public int solution(int left, int right) {
        /*
        1. 약수의 개수가 홀수 - 제곱수, 1일 경우
        2. 약수의 개수가 짝수 - 제곱수, 1을 제외한 모든 경우 
        3. 약수의 개수 짝수는 + , 홀수는 -
        */
        int sum = 0;
        
        for(int i = left; i < right+1; i++){
            //예) 13, 14, 15, 16, 17 
            if(Math.sqrt(i) % 1 == 0){
               sum = sum + i; 
            }
            else{
                sum = sum - i;
            }
        }
        
        return Math.abs(sum);
    }
}