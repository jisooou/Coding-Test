class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        // for(String str01 : s1){
        //     for(String str02 : s2){
        //         if(str01.equals(str02)){
        //             answer++;
        //         }
        //     }
        // }

        
        for(int i = 0; i < s1.length; i++){
            for(int j = 0; j < s2.length; j++){
                if(s1[i].equals(s2[j])){
                    answer++;
                }
            }
        }
    
        
        return answer;
    }
}