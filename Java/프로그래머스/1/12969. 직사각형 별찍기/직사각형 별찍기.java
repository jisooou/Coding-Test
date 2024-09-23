import java.util.Scanner;

class Solution {
    public static void main(String[] args) {
        /*
        가로 - n
        세로 - m 
        */
        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                System.out.print("*");
            }
            System.out.println();
        }
        
    }
}