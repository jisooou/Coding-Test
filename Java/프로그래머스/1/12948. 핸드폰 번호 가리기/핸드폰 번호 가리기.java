//substring 함수 사용
class Solution {
    public String solution(String phone_number) {
        String answer = "";
        
        //제한 조건
        if(phone_number.length() < 4 || phone_number.length() > 20){
            System.out.println("phone_number 다시 입력");
        }   
        
        for(int i = 0; i < phone_number.length()-4; i++){
            answer += "*";
        }
        
        answer += phone_number.substring(phone_number.length()-4);
        
        return answer;
    }
}