import java.util.Arrays; 

class Solution
{
    public int solution(int []A, int []B)
    {
        
        /*
        1. 
        */
        int sum = 0;
        
        Arrays.sort(A);
        Arrays.sort(B);
        
        
        for(int i = 0; i < A.length; i++){
            //A[0]*B[2] + A[1]*B[1] + A[2]*B[0]
            sum = sum + ( A[i] * B[B.length - 1 - i] );
        }

        return sum;
    }
}

//         for(int i = 0; i < A.length; i++){
//             for(int j = i; j < A.length; j++){
                
//                 if(A[i] > A[j]){
//                     int temp = A[i];
//                     A[i] = A[j];
//                     A[j] = temp; 
                    
//                 }
//             }
//         }