import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        double first = sc.nextInt();
        double second = sc.nextInt();
        double ans = first/second;
        System.out.println(ans);
    }
}