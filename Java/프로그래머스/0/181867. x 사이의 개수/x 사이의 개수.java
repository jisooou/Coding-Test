//split함수 사용 
class Solution {
    public int[] solution(String myString) {
        
        String[] find = myString.split("x", -1);
        
        int[] answer = new int[find.length];
        
        for(int i = 0; i < find.length; i++){
            answer[i] = find[i].length();
        }
         
        return answer;
    }
}