import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T=sc.nextInt();
        System.out.println((int)Math.pow((Math.pow(2,T)+1),2));
   }
}