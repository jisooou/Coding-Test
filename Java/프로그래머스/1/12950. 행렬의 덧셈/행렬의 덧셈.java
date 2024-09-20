class Solution {
    public int[][] solution(int[][] arr1, int[][] arr2) {
        /*
        1. 배열의 길이 선언
        2. arr1의 길이만큼 for문을 돌고, 
        3. arr1[i]의 길이만큼 for문을 돌고 
        4. answer에 arr1과 arr2값을 합친다.
        */
        int[][] answer = new int[arr1.length][arr1[0].length];
        
        for(int i = 0; i < arr1.length; i++){
            for(int j = 0; j < arr1[i].length; j++){
                answer[i][j] = arr1[i][j] + arr2[i][j];
            }
        }
         
        return answer;
    }
}