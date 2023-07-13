import java.io.IOException;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T=sc.nextInt();
        sc.nextLine();
        for(int i=0;i<T;i++){
            int n=sc.nextInt();
            String s=sc.nextLine();
            s=s.replace(" ","");
            for(int j=0;j<s.length();j++){
                for(int k=0;k<n;k++){
                    System.out.print(s.charAt(j));
                }
            }
            System.out.println();
        }
    }
}