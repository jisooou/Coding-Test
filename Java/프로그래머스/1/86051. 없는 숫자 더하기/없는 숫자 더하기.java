class Solution {
    public int solution(int[] numbers) {
        /*
        1. numbers 배열 순회하는 동안에
        2. 숫자 전부 합해서 sum에 저장 
        3. 0~9까지 숫자 합인 45 사용해서   
        4. 45 - sum = answer
        5. answer 값 리턴 
        */
        int sum = 0;
        for(int i = 0; i < numbers.length; i++){
            sum = sum + numbers[i];
        }
        int answer = 45 - sum; 
        
        return answer;
    }
}