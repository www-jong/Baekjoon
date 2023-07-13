import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int X = sc.nextInt();
        int res = 0;
        for(int i=0;i<N;i++){
            int tmp = sc.nextInt();
            if(tmp<X){
                System.out.print(tmp+" ");
                res++;
            }
        }
    }
}