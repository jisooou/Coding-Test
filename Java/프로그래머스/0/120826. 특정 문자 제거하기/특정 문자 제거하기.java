class Solution {
    public String solution(String my_string, String letter) {
        String answer = "";
        
        answer = my_string.replace(letter, "");
       
        return answer;
    }
}

//replace(기존 문자, 바뀔 문자) 