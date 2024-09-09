//split함수 사용 
class Solution {
    public int[] solution(String myString) {
        
        //split("x", 0) : x를 기준으로 나눔. 대신 마지막 공백은 나오지 않음. 
        String[] find = myString.split("x", -1);
        
        int[] answer = new int[find.length];
        
        for(int i = 0; i < find.length; i++){
            answer[i] = find[i].length();
        }
         
        return answer;
    }
}