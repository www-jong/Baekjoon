import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N=sc.nextInt();
        int M=sc.nextInt();
        sc.nextLine();
        int[][] A=new int[N][M];
        int[][] B=new int[N][M];
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                A[i][j]=sc.nextInt();
            }
            sc.nextLine();
        }
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                B[i][j]=sc.nextInt();
            }
            sc.nextLine();
        }
        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                System.out.print((A[i][j]+B[i][j])+" ");
            }
            System.out.println();
        }
        
    }
}