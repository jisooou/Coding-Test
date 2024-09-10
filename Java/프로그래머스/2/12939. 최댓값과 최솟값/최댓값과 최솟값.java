class Solution {
    public String solution(String s) {
        String answer = "";
        
        //공백을 기준으로 split > 배열 만들기
        String[] array = s.split(" ");
        
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE; 
        
        for(int i = 0; i < array.length; i++){
            //최소
            if(Integer.parseInt(array[i]) < min){
                min = Integer.parseInt(array[i]);
            }
            //최대
            if(Integer.parseInt(array[i]) > max){
                max = Integer.parseInt(array[i]);
            }
        }
        
        answer = Integer.toString(min) + " " + Integer.toString(max);
        
        return answer;
    }
}