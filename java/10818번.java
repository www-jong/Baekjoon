import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] s=new int[2];
        s[0]=10000000;
        s[1]=-10000000;
        for(int i=0;i<N;i++){
            int tmp=sc.nextInt();
            if(tmp>s[1]){
                s[1]=tmp;
            }
            if(tmp<s[0]){
                s[0]=tmp;
            }
        }
        System.out.print(s[0]+" "+s[1]);
    }
}