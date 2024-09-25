class Solution {
    public int[] solution(String s) {
        /*
        1. for문 
        2. 처음 나온 알파벳 > -1
        3. 나왔던 알파벳 > 가장 가까운 인덱스 
        */
        int[] answer = new int[s.length()];
        
        for(int i = 0; i < s.length(); i++){
            answer[i] = -1;
        }
        
        for(int i = 0; i < s.length(); i++){
            char index = s.charAt(i);
            
            for(int j = i-1; j >= 0; j--){
                if(s.charAt(j) == index){
                    answer[i] = i - j;
                    break;
                }
            }
        }
        
        return answer;
    }
}