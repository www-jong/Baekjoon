import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        String[] a=sc.nextLine().split(" ");

        System.out.println(Integer.toString(Integer.parseInt(a[0]),Integer.parseInt(a[1])).toUpperCase());
    }
}