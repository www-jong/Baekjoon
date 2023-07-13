import java.io.IOException;
import java.util.Scanner;
import java.math.BigInteger;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        BigInteger A = sc.nextBigInteger();
        BigInteger B = sc.nextBigInteger();
        BigInteger C = sc.nextBigInteger();
        System.out.println(A.add(B.add(C)));
    }
}