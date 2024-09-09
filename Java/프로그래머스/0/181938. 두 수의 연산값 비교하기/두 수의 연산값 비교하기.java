// 문자열로 변환,String.valueOf()와 정수형으로 변환,Integer.parseInt(str)
class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String stringSum = String.valueOf(a) + String.valueOf(b);
        int multi = 2 * a * b; 
        
        if(Integer.parseInt(stringSum) > multi){
            answer = Integer.parseInt(stringSum);
        }
        else if(Integer.parseInt(stringSum) < multi){
            answer = multi; 
        }
        
        return answer;
    }
}