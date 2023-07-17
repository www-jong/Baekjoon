import java.io.IOException;
import java.util.*;
import java.lang.Math;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int V = sc.nextInt();
        System.out.println(1+(int)Math.ceil((double)(V-A)/(A-B)));
    }
}