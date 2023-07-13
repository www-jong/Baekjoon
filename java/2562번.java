import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int[] res= {0,0};
        for(int i=1;i<=9;i++){
            int tmp=sc.nextInt();
            if(res[0]<tmp){
                res[0]=tmp;
                res[1]=i;
            }
        }

        System.out.println(res[0]);
        System.out.println(res[1]);
    }
}