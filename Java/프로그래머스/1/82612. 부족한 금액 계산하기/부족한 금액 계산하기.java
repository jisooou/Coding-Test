class Solution {
    public long solution(int price, int money, int count) {
        /*
            *long 타입
        1. 금액이 부족하지 않다면 0을 리턴
        2. for문이 count 만큼 도는 동안에 
        3. 예) 3, 6, 9, 12... price만큼 더해주는 식 구하고 
        4. 3번의 숫자들의 합을 total에 구한 후 
        5. total - money 계산해서 long타입으로 리턴 
        */
        long answer = -1;
        long sumPrice = 0;
        long total = 0;
        
        for(int i = 0; i < count; i++){
            //0, 1, 2, 3 > 각각 price가 3씩 sum에 더해짐.
            sumPrice = (long) sumPrice + price; 
            total = (long) total + sumPrice; 
        }
        
        answer = (long) total - money; 
        //금액이 부족하지 않을 경우 0을 리턴 
        if(answer <= 0){
            return 0;
        }

        return answer;
    }
}