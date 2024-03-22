class Solution {
    public int[] solution(int money) {
        //최대 아메리카노 잔 수 & 남는 돈
        int[] answer = new int[2];
        
        answer[0] = money / 5500;
            
        answer[1] = money - (5500 * answer[0]);
        //answer[1] = money % 5500;
        
        return answer;
    }
}