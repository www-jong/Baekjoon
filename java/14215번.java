import java.io.IOException;
import java.util.*;
import java.math.BigInteger;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int[] tmp={a,b,c};
        Arrays.sort(tmp);
        a=tmp[0];
        b=tmp[1];
        c=tmp[2];
        int res = -1;
        if(a+b>c){
            res=(res>a+b+c)?res:a+b+c;
        }
        if(a==b&&b==c){
            res=(res>a*3)?res:a*3;
        }
        if(a+b<=c){
            res=(res>(a+b)*2-1)?res:(a+b)*2-1;
        }
        System.out.println(res);
    }
}