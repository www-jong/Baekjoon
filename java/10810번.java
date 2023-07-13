import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] res= new int[N];
        for(int i=0;i<N;i++){
            res[i]=0;
        }
        for(int i=0;i<M;i++){
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
            for(int j=A;j<=B;j++){
                res[j-1]=C;
            }
        }
        for(int i=0;i<N;i++){
            System.out.print(res[i]+" ");
        }
    }
}