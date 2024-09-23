class Solution {
    public int solution(int n) {
        /*
        1.주어진 n을 
        2.for문을 통해 몫이 0이 될 때까지 3으로 나누기
        3.2번을 뒤집는다
        4.3번의 각 숫자에 3의 0,1,2,3 제곱을 한다
        */
        int answer = 0;
        String result = "";
    
        while(n != 0){
            int remain = n % 3; 
            result = remain + result;
            n = n / 3;
        }

        for(int i = 0; i < result.length(); i++){
            int number = result.charAt(i) - '0';
            answer += number * Math.pow(3, i);
        }
        
        return answer;
    }
}