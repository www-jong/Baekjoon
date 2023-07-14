import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int T=sc.nextInt();
        sc.nextLine();
        for(int i=0;i<T;i++){
            int C=Integer.parseInt(sc.nextLine());
            int[] a=new int[4];
            a[0]=C/25;
            a[1]=C%25/10;
            a[2]=C%25%10/5;
            a[3]=C%25%10%5/1;
            System.out.println(a[0]+" "+a[1]+" "+a[2]+" "+a[3]);
            
        }

   }
}