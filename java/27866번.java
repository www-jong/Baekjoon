import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        String A = sc.nextLine();
        int B = sc.nextInt();

        System.out.println(A.charAt(B-1));
    }
}