class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        
        /*
        for문 3번 돌리면서 
        photo 배열에 name 배열이 얼마나 일치하는지 확인 
        일치하는 횟수만큼 yearning에서 합 구하기 
        */
        int[] answer = new int[photo.length];
        
        for(int i = 0; i < photo.length; i++){
            int sum = 0; 
            
            for(int j = 0; j < photo[i].length; j++){
                String person = photo[i][j];
                
                for(int k = 0; k < name.length; k++){
                    if(person.equals(name[k])){
                        sum = sum + yearning[k];
                    }
                }
            }
            answer[i] = sum; 
        }
        return answer;
    }
}