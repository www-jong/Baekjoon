import java.io.IOException;
import java.util.Scanner;
import java.util.ArrayList;
public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        
        int res= 0;
        int N = sc.nextInt();
        int[] li= new int[N];
        for(int i=0;i<N;i++){
            li[i]=sc.nextInt();
        }
        int S = sc.nextInt();
        for(int i=0;i<N;i++){
            if(li[i]==S){
                res+=1;
            }
        }
        System.out.println(res);
    }
}