class Solution {
    public String solution(String s) {
        /*
        단어 공백 기준으로 짝/홀수 인덱스
        1.짝수번째 - 대문자
        2.홀수번째 - 소문자
        3.공백
        */
        String answer = "";
        String[] array = s.split("");
        int index = 0;
        
        for(int i = 0; i < array.length; i++){
            if(array[i].equals(" ")){
                index = 0;
            }
            
            else if(index % 2 == 0){
                array[i] = array[i].toUpperCase(); 
                index++;
            }
            else if(index % 2 == 1){
                array[i] = array[i].toLowerCase();
                index++;
            }
            answer += array[i];
        }
        
        return answer;
    }
}