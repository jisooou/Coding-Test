class Solution {
    public int[] solution(int[] numbers) {
        //ArrayOutOfBound가 나오지 않도록 
        //배열을 처음~numbers의 길이만큼 초기화 시켜준다. 
        int[] answer = new int[numbers.length];
        
        for(int i = 0; i < numbers.length; i++){
            answer[i] = numbers[i] * 2;
        }
        
        return answer;
    }
}