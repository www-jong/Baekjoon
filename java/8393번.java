import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        System.out.println((int)((A%2==0)?(1+A)*(A/2):(1+A)*(A/2+0.5)));
    }
}