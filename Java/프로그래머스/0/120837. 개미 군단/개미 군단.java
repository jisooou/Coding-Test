//장군-5
//병정-3
//일-1
class Solution {
    public int solution(int hp) {
        int answer = 0;
        
        int a = 5; 
        int b = 3; 
        int c = 1;
        
        answer = (hp/a) + ((hp%a)/b) + ((hp%a)%b);
        
        return answer;
    }
}