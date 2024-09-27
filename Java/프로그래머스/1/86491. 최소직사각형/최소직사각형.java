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
        int widthMax = 0; 
        int heightMax = 0;
         for (int i = 0; i < sizes.length; i++) {
            if (sizes[i][0] > widthMax) {
                widthMax = sizes[i][0];
            }
            if (sizes[i][1] > heightMax) {
                heightMax = sizes[i][1];
            }
        }
        answer = widthMax * heightMax; 
        
        return answer;
    }
}