class Solution {
    public String solution(String s) {
        String answer = "";
        
        //단어의 길이가 홀수인 경우
        for(int i = 0; i < s.length(); i++){
            int mid = (s.length() / 2);
            answer = String.valueOf(s.charAt(mid));
            
            //단어의 길이가 짝수인 경우
            if(s.length() % 2 == 0){
                String first = String.valueOf(s.charAt(mid-1)); //첫번째단어
                String second = String.valueOf(s.charAt(mid)); //두번째단어
                String result = first + second; 
                answer = result; 
            }
        }
        
        return answer;
    }
}