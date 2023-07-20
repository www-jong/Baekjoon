import java.io.IOException;
import java.util.*;
import java.math.BigInteger;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int A=sc.nextInt();
        int B=sc.nextInt();
        int C=sc.nextInt();
        String res = "";
        if(A==60&&B==60&&C==60){
            res="Equilateral";
        }else if(A+B+C==180){
            if(A==B||B==C||A==C){
                res="Isosceles";
            }else{
                res="Scalene";
            }
        }else{
            res="Error";
        }
        System.out.println(res);
    }
}