// 인덱스를 출력하는 문제 
class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        
//      indexOf는 "String 클래스"에서 사용O ("String 배열"에서 사용X)
//      equals는 전부 사용 가능O
        for(int i = 0; i < seoul.length; i++){
            if(seoul[i].equals("Kim")){
                answer = "김서방은 " + i + "에 있다";
            }
        }
        
        return answer;
    }
}