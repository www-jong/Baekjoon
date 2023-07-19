import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N=sc.nextInt();
        int B=sc.nextInt();
        int c=0;
        int res=0;
        for(int i=1;i<=N;i++){
            if(N%i==0){
                c+=1;
            }
            if(c==B){
                res=i;
                break;
            }
        }
        System.out.println(res);
    }
}