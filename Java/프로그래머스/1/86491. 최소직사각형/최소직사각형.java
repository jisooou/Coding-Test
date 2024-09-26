class Solution {
    public int solution(int[][] sizes) {
        /*
            (가로,세로) - 가로와 세로를 비교해서 더 작은 수를 가로에 다 모은 후, 
            가로에서 최댓값 * 세로에서 최댓값 = 답 
        */
        int answer = 0; 
        
        for(int i = 0; i < sizes.length; i++){
                
                //[가로,세로] - 가로 > 세로 일 때 
                if(sizes[i][0] > sizes[i][1]){
                    int temp = sizes[i][0];
                    sizes[i][0] = sizes[i][1];
                    sizes[i][1] = temp; 
                }
        }
        
        //전체 배열에서 가로의 최대값 * 세로의 최대값
        int max = 0; 
        int min = 0;
         for (int i = 0; i < sizes.length; i++) {
            if (sizes[i][0] > max) {
                max = sizes[i][0];
            }
            if (sizes[i][1] > min) {
                min = sizes[i][1];
            }
        }
        // for(int x = 0; x < sizes.length; x++){
        //     for(int y = 0; y < sizes[x].length; y++){
        //         if(y[0] > max){
        //             max = y[0];
        //         }
        //         if(y[1] < min){
        //             min = y[1];
        //         }
        //     }
        // }
        answer = max * min; 
        
        return answer;
    }
}