import java.io.IOException;
import java.util.*;
import java.math.BigInteger;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N=sc.nextInt();
        //sc.nextLine();
        long x1=100000;
        long y1=100000;
        long x2=-100000;
        long y2=-100000;
        for(int i=0;i<N;i++){
            long a=sc.nextInt();
            long b=sc.nextInt();
            x1=(x1<a)?x1:a;
            y1=(y1<b)?y1:b;
            x2=(x2>a)?x2:a;
            y2=(y2>b)?y2:b;
            
        }
        System.out.println((x2-x1)*(y2-y1));
    }
}