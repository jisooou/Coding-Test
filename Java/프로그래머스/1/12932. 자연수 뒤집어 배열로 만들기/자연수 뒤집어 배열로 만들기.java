class Solution {
    public int[] solution(long n) {
        
        /*
        1. n의 길이 구하기 
        2. 배열 크기를 n의 길이만큼 지정하기 
        3. %10, /10을 통해 n을 뒤집기 
        4. 배열에 각 숫자 저장하기 
        */
        
        int len = Long.toString(n).length();
        
        int[] answer = new int[len];
        
        for(int i = 0; i < len; i++){
            answer[i] = (int) (n % 10);
            n = n / 10; 
        }
        
        return answer;
    }
}