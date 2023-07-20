import java.io.IOException;
import java.util.*;
import java.math.BigInteger;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        while(true){
            int A=sc.nextInt();
            int B=sc.nextInt();
            int C=sc.nextInt();
            String res = "";
            if(A==0&&B==0&&C==0){break;}
            int[] tmp={A,B,C};
            Arrays.sort(tmp);
            if(tmp[0]+tmp[1]<=tmp[2]){
                res="Invalid";
            }
            else if(A==B&&B==C){
                res="Equilateral";
            }else if(A==B||B==C||A==C){
                res="Isosceles";
            }else{
                res="Scalene";
            }
            System.out.println(res);
        }
    }
}