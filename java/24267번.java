import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        long N =(long) sc.nextInt();
        long res = 1;
        if(N<=2){
            System.out.println(0);
        }else{
            for(long i=4;i<=N;i++){
                res+=(long)((i-1)*(i-2)/2);
            }
            System.out.println(res);
        }
        System.out.println(3);
        
    }
}